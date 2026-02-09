import pytest

def test_login():
    print("test 1")
    assert 1==0

@pytest.mark.smoke
def test_method():
    print("test 2")
    assert 1==1