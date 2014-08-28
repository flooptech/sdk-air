# (C) Ululab, all rights reserved

"""
Allows us to build Adobe AIR applications into iOS packages. 

This is based on the PackageApp.bat batch file from FlashDevelop. 

We needed to improve those scripts and DOS batch files are not exactly the most maintainable file types 
so this Python application tries to do a similar job for iOS devices. 

"""

import sys
import os
import winsound
import paths
import proc
import netutils

class iOSBuildPackage:
	BUILD_TYPE_IOS_INTERPRETER_DEBUG 	= 1
	BUILD_TYPE_IOS_INTERPRETER_RELEASE 	= 2
	BUILD_TYPE_IOS_NATIVE_DEBUG 		= 3
	BUILD_TYPE_IOS_NATIVE_RELEASE 		= 4
	BUILD_TYPE_IOS_AD_HOC 				= 5
	BUILD_TYPE_IOS_APP_STORE 			= 6

	BUILD_TYPE_MIN				= BUILD_TYPE_IOS_INTERPRETER_DEBUG
	BUILD_TYPE_MAX				= BUILD_TYPE_IOS_APP_STORE
	
	# Name of the distribution, used for the filename
	DIST_NAME = "Demo"
	
	# Adobe Air Application manifest.
	APP_XML = "application.xml"
	
	# Input application binary file (where the SWF and the resources are).
	APP_DIR = "bin"
	
	# Application icons
	ICONS_PATH = paths.IOS_ICONS
	
	# output_path: Path where to output the distribution package file.
	# use_sampler: Set to true to package with the -sampler flag. The -sampler flag will allow advanced telemetry for 
	# 				the Adobe Scout Profiler. 
	def __init__(self, ios_dev_cert_file, ios_dev_cert_password, ios_provision, output_path, use_sampler=False):
		self.ios_dev_cert_file = ios_dev_cert_file
		self.ios_dev_cert_password = ios_dev_cert_password
		self.ios_provision = ios_provision
		self.output_path = output_path
		self.use_sampler = use_sampler
		
		self.type = {}
		self.type[self.BUILD_TYPE_IOS_INTERPRETER_DEBUG] = "ipa"
		self.type[self.BUILD_TYPE_IOS_INTERPRETER_RELEASE] = "ipa"
		self.type[self.BUILD_TYPE_IOS_NATIVE_DEBUG] = "ipa"
		self.type[self.BUILD_TYPE_IOS_NATIVE_RELEASE] = "ipa"
		self.type[self.BUILD_TYPE_IOS_AD_HOC] = "ipa"
		self.type[self.BUILD_TYPE_IOS_APP_STORE] = "ipa"
			
		self.dist_ext = {}
		self.dist_ext[self.BUILD_TYPE_IOS_INTERPRETER_DEBUG] = "ipa"
		self.dist_ext[self.BUILD_TYPE_IOS_INTERPRETER_RELEASE] = "ipa"
		self.dist_ext[self.BUILD_TYPE_IOS_NATIVE_DEBUG] = "ipa"
		self.dist_ext[self.BUILD_TYPE_IOS_NATIVE_RELEASE] = "ipa"
		self.dist_ext[self.BUILD_TYPE_IOS_AD_HOC] = "ipa"
		self.dist_ext[self.BUILD_TYPE_IOS_APP_STORE] = "ipa"
		
		self.target = {}
		self.target[self.BUILD_TYPE_IOS_INTERPRETER_DEBUG] = "-debug-interpreter"
		self.target[self.BUILD_TYPE_IOS_INTERPRETER_RELEASE] = "-test-interpreter"
		self.target[self.BUILD_TYPE_IOS_NATIVE_DEBUG] = "-debug"
		self.target[self.BUILD_TYPE_IOS_NATIVE_RELEASE] = "-test"
		self.target[self.BUILD_TYPE_IOS_AD_HOC] = "-ad-hoc"
		self.target[self.BUILD_TYPE_IOS_APP_STORE] = "-app-store"
		
		self.options = {}
		self.options[self.BUILD_TYPE_IOS_INTERPRETER_DEBUG] = "-connect " + netutils.get_ipaddress()
		self.options[self.BUILD_TYPE_IOS_INTERPRETER_RELEASE] = ""
		self.options[self.BUILD_TYPE_IOS_NATIVE_DEBUG] = "-connect " + netutils.get_ipaddress()
		self.options[self.BUILD_TYPE_IOS_NATIVE_RELEASE] = ""
		self.options[self.BUILD_TYPE_IOS_AD_HOC] = ""
		self.options[self.BUILD_TYPE_IOS_APP_STORE] = ""
		
		self.needs_cert_password = {}
		self.needs_cert_password[self.BUILD_TYPE_IOS_INTERPRETER_DEBUG] = True
		self.needs_cert_password[self.BUILD_TYPE_IOS_INTERPRETER_RELEASE] = True
		self.needs_cert_password[self.BUILD_TYPE_IOS_NATIVE_DEBUG] = True
		self.needs_cert_password[self.BUILD_TYPE_IOS_NATIVE_RELEASE] = True
		
		# DJOLY:TODO: We might need to use a password here, otherwise it doesn't build
		self.needs_cert_password[self.BUILD_TYPE_IOS_AD_HOC] = True	# SetupApplication.bat uses a different cert, and no password for those build types
		self.needs_cert_password[self.BUILD_TYPE_IOS_APP_STORE] = True	# SetupApplication.bat uses a different cert, and no password for those build types
		
	def init_from_user(self):
		done = False
		while not done:
			
			try:
				self._print_build_types()
				build_type = int(input())
				
				if self._is_valid_build_type(build_type):
					done = True
			except ValueError:
				pass
		
		self.build_type = build_type
		
	def build_package(self):
		command = self._build_command(self.ios_dev_cert_password)
		command_to_print = self._build_command("<hidden password>")
		print(command_to_print)
		paths.setup_environment_for_ios()
		print()
		if not os.path.exists(self.output_path):
			print("Creating output folder ( " + self.output_path + " )...")
			os.makedirs(self.output_path)
			print()
		sys.stdout.write("Wait for it...     ")
		sys.stdout.flush()
		stdout, stderr, returncode = proc.run(command)
		
		if len(stderr) == 0:
			print("Done!")
		else:
			print("stdout: " + stdout.decode(encoding="UTF-8"))
			print("stderr: " + stderr.decode(encoding="UTF-8"))
		print()
		print("Go get your package in: " + self.output_path)
		winsound.PlaySound('C:\\Windows\\Media\\tada.wav', winsound.SND_FILENAME)
		
	def _print_build_types(self):
		print("----------------------------------")
		print("Adobe Air iOS build - Ululab Inc.")
		print("----------------------------------")
		print("[1] iOS Interpreter (fast build), WITH auto-debugger-connect      (ipa-debug-interpreter)")
		print("[2] iOS Interpreter (fast build), NO debugger support             (ipa-test-interpreter)")
		print("[3] iOS Native compile (slow build), WITH auto-debugger-connect   (ipa-debug)")
		print("[4] iOS Native compile (slow build), NO debugger support          (ipa-test)")
		print()
		print()
		print("[5] iOS Native compile AD-HOC                                     (ipa-ad-hoc)")
		print("[6] iOS Native compile APP STORE                                  (ipa-app-store)")
		print()
	def _is_valid_build_type(self, build_type):
		return build_type >= self.BUILD_TYPE_MIN and build_type <= self.BUILD_TYPE_MAX
		
	def _build_command(self, password):
		output_file_name = self.DIST_NAME + self.target[self.build_type] + "." + self.dist_ext[self.build_type]
		output = os.path.join(self.output_path, output_file_name)
		file_or_dir = "-C " + self.APP_DIR + " . -C " + self.ICONS_PATH + " ."
		dev_signing_options = "-storetype pkcs12 -keystore \"" + self.ios_dev_cert_file + "\" -provisioning-profile " + self.ios_provision
		if self.needs_cert_password[self.build_type]:
			dev_signing_options = dev_signing_options + " -storepass \"" + password + "\""
		use_sampler_opt = ""
		if self.use_sampler:
			use_sampler_opt = "-sampler"
		
		# -extdir NativeLib: Use native extensions
		return "adt -package -target " + self.type[self.build_type] + self.target[self.build_type] + " " + self.options[self.build_type] + " " + use_sampler_opt + " " + dev_signing_options + " " + output + " " + self.APP_XML + " " + file_or_dir + " -extdir NativeLib"
		
	
def print_man():
	print("Usage: package_app_ios.py <ios_dev_cert_file.cert> <ios_dev_cert_password> <ios_provision.mobileprovision>")
	
if __name__ == '__main__':
	if len(sys.argv) < 5:
		print_man()
		quit()
		
	ios_dev_cert_file = sys.argv[1]
	ios_dev_cert_password = sys.argv[2]
	ios_provision = sys.argv[3]
	output_path = sys.argv[4]
	builder = iOSBuildPackage(ios_dev_cert_file, ios_dev_cert_password, ios_provision, output_path)
	builder.init_from_user()
	builder.build_package()
	