import pytest
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json"
}

def get_booking_id():
    base_path="/booking"
    full_url=base_url+base_path


    payload= {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

    response_data=requests.post(url=full_url, json=payload, headers=headers)
    response_data_json=response_data.json()
    print(response_data_json)
    bookingid=response_data_json["bookingid"]
    return (bookingid)

def get_token():
    base_path = "/auth"
    full_url = base_url + base_path

    payload = {
        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(url=full_url, headers=headers, json=payload)
    response_token_json = response_data.json()
    token = response_token_json["token"]
    return token

def test_put_req():
    booking_id= get_booking_id()
    print(booking_id)
    token = get_token()
    print(token)
    base_path="/booking/"+str(booking_id)
    full_url=base_url+base_path
    print(full_url)
    cookie="token="+token
    headers = {
        "Content-Type": "application/json",
        "cookie": cookie
    }

    payload={
    "firstname" : "Nitha",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

    response=requests.put(url=full_url, json=payload, headers=headers)
    #print(response.text)
    #assert response.status_code == 200
    response_data=response.json()
    print(response_data)
    #assert response_data.firstname=="Nitha"