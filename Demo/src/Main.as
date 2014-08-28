package 
{
	import com.ululab.nativeExtensions.floopsdk.floopsdk;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.ui.Multitouch;
	import flash.ui.MultitouchInputMode;
	
	public class Main extends Sprite 
	{
		
		public function Main():void 
		{
			stage.scaleMode = StageScaleMode.NO_SCALE;
			stage.align = StageAlign.TOP_LEFT;
			stage.addEventListener(Event.DEACTIVATE, deactivate);
			
			// touch or gesture?
			Multitouch.inputMode = MultitouchInputMode.TOUCH_POINT;
			
			// Cheap button
			var rectangle:Sprite = new Sprite();
			rectangle.graphics.beginFill(0xff0000);
			rectangle.graphics.drawRoundRect(0, 0, 450, 350, 40);
			rectangle.graphics.endFill();
			rectangle.x = 100;
			rectangle.y = 350;
			
			var textFormat:TextFormat = new TextFormat(null, 36);
			var text:TextField = new TextField();
			text.text = "Launch Floop!";
			text.width = 300;
			text.setTextFormat(textFormat);
			text.x = 125;
			text.y = 150;
			
			rectangle.addChild(text);
			this.addChild(rectangle);
			
			floopsdk.init();
			if (!floopsdk.isSupported)
			{
				trace("ERROR: Could not create floopsdk context");
			}
			
			rectangle.addEventListener(MouseEvent.CLICK, launchFloop, false, 0, true);
		}
		
		private function deactivate(e:Event):void 
		{
			// make sure the app behaves well (or exits) when in background
			//NativeApplication.nativeApplication.exit();
		}
		
		private function launchFloop(e:Event):void
		{
			if (floopsdk.isSupported)
			{
				floopsdk.startWithAppKey("91be365cf0a4c0b8df78bbb9fd8248bc");
				floopsdk.showParentalGate();
			}
		}
	}
	
}