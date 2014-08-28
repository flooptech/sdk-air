#import <Foundation/Foundation.h>
#import "FlashRuntimeExtensions.h"
#import "floopsdk_TypeConversion.h"

#import <UIKit/UIKit.h>
#import <floopsdk/FloopSdk.h>

#define DEFINE_ANE_FUNCTION(fn) FREObject (fn)(FREContext context, void* functionData, uint32_t argc, FREObject argv[])

#define MAP_FUNCTION(fn, data) { (const uint8_t*)(#fn), (data), &(fn) }

floopsdk_TypeConversion* floopsdkTypeConverter;

DEFINE_ANE_FUNCTION(floopsdk_startWithAppKey)
{
    NSString* appKey;
    if([floopsdkTypeConverter FREGetObject:argv[0] asString:&appKey ] == FRE_OK)
    {
        [[FloopSdkManager sharedInstance] startWithAppKey:appKey];
    }
    return NULL;
}

void floopsdkContextInitializer(void* extData, const uint8_t* ctxType, FREContext ctx, uint32_t* numFunctionsToSet, const FRENamedFunction** functionsToSet)
{
    static FRENamedFunction functionMap[] = {
        MAP_FUNCTION(floopsdk_startWithAppKey, NULL),
    };
    
	*numFunctionsToSet = sizeof(functionMap) / sizeof(FRENamedFunction);
	*functionsToSet = functionMap;
    
    floopsdkTypeConverter = [[floopsdk_TypeConversion alloc] init];
    
    NSLog(@"floopsdkContextInitializer registered");
}

void floopsdkContextFinalizer(FREContext ctx)
{
	return;
}

void floopsdkExtensionInitializer(void** extDataToSet, FREContextInitializer* ctxInitializerToSet, FREContextFinalizer* ctxFinalizerToSet)
{ 
    extDataToSet = NULL;  // This example does not use any extension data. 
    *ctxInitializerToSet = &floopsdkContextInitializer;
    *ctxFinalizerToSet = &floopsdkContextFinalizer;
}

void floopsdkExtensionFinalizer()
{
    return;
}
