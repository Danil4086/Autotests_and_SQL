import requests
from configuration import URL_SERVICE, CREATE_ORDER, GET_ORDER_TRACK


def test_order_api():
    track_number = create_order()

    response_code = get_order_by_track(track_number)

    assert response_code == 200


def create_order():
    url = URL_SERVICE + CREATE_ORDER
    order = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    response = requests.post(url, json=order)

    assert response.status_code == 201, "Успешное создание заказа"

    track_number = response.json().get("track")
    assert track_number == 200

    return track_number


def get_order_by_track(track_number):
    url = URL_SERVICE + GET_ORDER_TRACK + "?t=" + str(track_number)
    response = requests.get(url)

    return response.status_code
