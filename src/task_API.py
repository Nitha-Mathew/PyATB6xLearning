import random
import time

API_call_time=3
response_code=random.choice([500,200,500])
while API_call_time>0:
    print(response_code)
    if (response_code==200):
        print("API successful")
        break
    else:
        print("Wait...Trying to connect..")
    time.sleep(1)
    API_call_time=API_call_time-1
if API_call_time<=0:
    print("API failed")

