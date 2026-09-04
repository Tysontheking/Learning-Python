import time
import asyncio
from plyer import notification
# from desktop_notifier import DesktopNotifier

# notifier = DesktopNotifier()
# async def Timer():
#     # print("You are working to hard just take a break and sip some water")
#     await notifier.send(title="Take some break",message="You are working to hard just take a break and sip some water")
#     time.sleep(2)
    
# asyncio.run(Timer())

while True:
    print("You are working to hard just take a break and sip some water")
    notification.notify(title='Take some break',
                        message="You are working to hard just take a break and sip some water")
    time.sleep(60*60) #1 hour