# (C) Ululab, all rights reserved

import os

try:
	_PROGRAM_FILES = os.environ["ProgramFiles(x86)"]
except:
	_PROGRAM_FILES = os.environ["ProgramFiles"]

FLEX_SDK = _PROGRAM_FILES + "\\FlashDevelop\\Tools\\flexsdk\\bin"
ANDROID_SDK = _PROGRAM_FILES + "\\FlashDevelop\\Tools\\Android\\platform-tools"

IOS_ICONS="icons\\ios"
ANDROID_ICONS="icons\\android"

def setup_environment_for_ios():
	os.environ['PATH'] = os.environ['PATH'] + ";" + FLEX_SDK

	
def setup_environment_for_android():
	os.environ['PATH'] = os.environ['PATH'] + ";" + FLEX_SDK
	os.environ['PATH'] = os.environ['PATH'] + ";" + ANDROID_SDK
	
if not os.path.exists(FLEX_SDK):
	raise Exception("Flex SDK path doesn't exists: " + FLEX_SDK)
	
if not os.path.exists(ANDROID_SDK):
	raise Exception("Android SDK path doesn't exists: " + ANDROID_SDK)