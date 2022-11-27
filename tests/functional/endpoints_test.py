import requests
import json


def test_search_book():

    url = "http://localhost:5000/api/v1/books"

    params = {
        "title": "A Treatise Concerning"
    }

    response = requests.request("GET", url, params=params)

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()['books']

def test_create_review():

    book_id = 84
    url = f"http://localhost:5000/api/v1/books/{book_id}/review"

    payload = json.dumps({
        "bookId": book_id,
        "rating": 5,
        "description": "Very good book"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["data"]

def test_get_book_details():

    book_id = 84
    url = f"http://localhost:5000/api/v1/books/{book_id}"


    response = requests.request("GET", url)

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["books"]

