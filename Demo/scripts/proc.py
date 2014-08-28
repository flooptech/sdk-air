# (C) Ululab, all rights reserved

import subprocess
import time
import sys

class Timeout(Exception):
    pass

def run(command):
	proc = subprocess.Popen(command, shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = proc.communicate()
	return stdout, stderr, proc.returncode

def run_command_with_console(command):
	print("Run: " + command)
	stdout, stderr, errno = run(command)

	print()
	if len(stdout) > 0:
		print("stdout: " + stdout.decode(encoding="UTF-8"))
		
	if len(stderr) > 0:
		print("stderr: " + stderr.decode(encoding="UTF-8"))
		
	return errno
	
if __name__=="__main__":
	if len(sys.argv) >= 2:
		print(run_command_with_console(sys.argv[1]))