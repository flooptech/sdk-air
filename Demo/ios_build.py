# (C) Ululab, all rights reserved

"""
Will build a package.
"""
import sys
import os

# This allows us to open Python modules from the 'script' subdirectory
sys.path.append("scripts")
import package_app_ios

if __name__ == '__main__':
	print("Enter iOS dev certificate password: ")
	ios_dev_cert_password = input()
	os.system("cls")	# Clear the screen on Windows
	ios_dev_cert_file = "cert\\ios_development_signing_cert.p12"
	ios_provision = "cert\\DemoApp.mobileprovision"
	output_path = "dist"
	use_sampler = True
	builder = package_app_ios.iOSBuildPackage(ios_dev_cert_file, ios_dev_cert_password, ios_provision, output_path, use_sampler)
	builder.init_from_user()
	builder.build_package()
	print()
	print("Press any key to continue...")
	input()