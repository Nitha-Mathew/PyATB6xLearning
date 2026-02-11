import requests
import pytest

base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json"
}
base_path = "/booking"

def get_booking_id():
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

def test_delete():
    full_url=base_url+base_path+str(get_booking_id())

    response=requests.delete(url=full_url, headers=headers)
    assert response.status_code==200
