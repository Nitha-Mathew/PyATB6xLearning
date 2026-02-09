import requests
import pytest

@pytest.mark.positive
def test_get_booking():
    url="https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code==200

@pytest.mark.negative
def test_get_booking_negative():
    url="https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url)
    assert response_data.status_code==404