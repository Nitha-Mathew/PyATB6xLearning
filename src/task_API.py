API_call_time=3
response_code=500
while API_call_time>0:
    if (response_code==200):
        print("API successful")
        break
    else:
        print("API failed")
    API_call_time=API_call_time-1

