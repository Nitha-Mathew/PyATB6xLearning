import pytest
import requests

@pytest.mark.positive
def test_post_request():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"
    full_url=base_url+base_path

    headers={
        "Content-Type" :"application/json"
    }

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
    print(response_data)
    assert response_data.status_code==200

    response_data_json=response_data.json()
    print(response_data_json)
    bookingid=response_data_json["bookingid"]
    print (bookingid)
    firstname=response_data_json["booking"]["firstname"]
    print(firstname)

    #assertions
    assert type(firstname)==str
    assert bookingid >0
    time=response_data.elapsed.total_seconds()
    assert time<3

@pytest.mark.negative
def test_post_neg_req():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/booking"
    full_url=base_url+base_path

    headers={
        "Content-Type" :"application/json"
    }

    payload={}

    response_data=requests.post(url=full_url, headers=headers,json=payload)
    assert response_data.status_code==500

pytest.mark.token
def test_create_auth():
    base_url="https://restful-booker.herokuapp.com"
    base_path="/auth"
    full_url=base_url+base_path

    payload={
    "username" : "admin",
    "password" : "password123"
}

    headers={
        "Content-Type" :"application/json"
    }

    response_data=requests.post(url=full_url,headers=headers,json=payload)
    print(response_data)
    response_token_json=response_data.json()
    token=response_token_json["token"]
    print(token)
    #assert response_data.status_code == 200

