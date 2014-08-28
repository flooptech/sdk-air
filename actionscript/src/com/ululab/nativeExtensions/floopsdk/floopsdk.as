package com.ululab.nativeExtensions.floopsdk
{
	import flash.external.ExtensionContext;

	public class floopsdk
	{
		private static var _extensionContext : ExtensionContext = null;
		
		public static function init():void
		{
			if (_extensionContext == null)
			{
				_extensionContext = ExtensionContext.createExtensionContext( "com.ululab.nativeExtensions.floopsdk", null );
			}
			else
			{
				trace("floopsdk native extension context not available.");
			}
		}
		
		public static function get isSupported():Boolean
		{
			return _extensionContext ? true : false;
		}
		
		public static function startWithAppKey(appKey:String):void
		{
			if (_extensionContext != null)
			{
				_extensionContext.call(NativeMethods.startWithAppKey, appKey);
			}
		}
		
		public static function dispose() : void
		{
			if (_extensionContext)
			{
				_extensionContext.dispose();
				_extensionContext = null;
			}
		}
	}
}

