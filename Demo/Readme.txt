This is a generic FlashDevelop Mobile AS3 project that will launch the FloopSDK extension when clicking on the main red square. 

Intructions (Windows)
1. Install FlashDevelop from: http://www.flashdevelop.org/
2. Make sure your PATH contains the FlexSDK bin (c:\Program Files (x86)\FlashDevelop\Tools\flexsdk\bin)
3. Install Python 3.X: https://www.python.org/
4. Make sure Python is in your PATH
5. Launch Demo.as3proj
6. Edit application.xml
7.   Replace <id>com.DEMO_COMPANY.Demo</id> by an ID that matches an iOS certificate that you control
8. Add your P12 certificate and your .mobileprovision files to the "cert" folder
9. Edit ios_build.py 
10.   Modify the ios_dev_cert_file and ios_provision to point to your files
10. Build the project in DEBUG (F8)
11. Launch ios_build.py (Right click -> Execute)
12. Enter your cert password, if any. 
13. Choose "1" 
	Note: If you want to build in RELEASE so that you don't have to attach the debugger, choose option "2"
14. Install the IPA file in the "dist" folder (option 1 creates Demo-debug-interpreter.ipa). You now have Demo on your phone. 
15. Because you build in DEBUG mode, with option 1 DEBUG-interpreter, you will need the debugger to be launched to launch the App. In FlashDevelop: Debug -> Start Remote Session
16. Put a breakpoint if you want


Note: don't understand how to get the P12 and mobileprovision files? 
	http://www.emanueleferonato.com/2011/09/22/creation-of-an-iphone-app-with-flash-and-without-a-mac-for-all-windows-lovers/ 
	

I know this is a lot of steps. While they end up working OK, FlashDevelop & Adobe Air are not a smooth mobile environment. 

Good luck, 

Dany