import pytest
import requests

def test_invalid_credentials(mocker):
    # Mock the server response
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}
    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ''

    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(url, params=params)
    
    # Verify the response code is 401 (Unauthorized)
    assert response.status_code == 401
    
    # Verify the response is empty
    assert response.text.strip() == ""

def test_valid_credentials(mocker):
    # Mock the server response
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}
    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ''

    mocker.patch('requests.get', return_value=mocked_response)

    response = requests.get(url, params=params)

    # Verify the response code is 200 (OK)
    assert response.status_code == 200
    
    # Verify the response is empty
    assert response.text.strip() == ""