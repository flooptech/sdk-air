#import <Foundation/Foundation.h>
#import "FlashRuntimeExtensions.h"

@interface floopsdk_TypeConversion : NSObject

- (FREResult) FREGetObject:(FREObject)object asString:(NSString**)value;
- (FREResult) FREGetString:(NSString*)string asObject:(FREObject*)asString;

@end
