import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
#from gpiozero import Button
from time import sleep
 
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-1575c412-2116-11e8-a7d0-2e884fd949d2"
pnconfig.publish_key = "pub-c-2d8f55f6-daa7-467b-923b-6a1e6570c9fc"
pnconfig.ssl = False
 
pubnub = PubNub(pnconfig)


def publish_callback(result, status):
    pass
    # Handle PNPublishResult and PNStatus
 


button = Button(5)

tweet = "Hello World"
msg = { "tweet" : tweet }


while True:
    if button.is_pressed:
        print("Pressed")
        pubnub.publish().channel('twitter-input').message(msg).async(publish_callback)
    else:
        print("Released")
    sleep(1)




