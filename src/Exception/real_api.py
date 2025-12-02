import requests

try:
    url=input("Enter the url")
    response=requests.get(url)
    print(response.status_code)
except requests.exceptions.ConnectionError:
    print("connection error")
except Exception as e:
    print(e)
else:
    print("page loaded successfully")


