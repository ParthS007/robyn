import os

import requests

from helpers.network_helpers import get_network_host


def test_default_url_index_request(default_session):
    BASE_URL = "http://127.0.0.1:8080"
    res = requests.get(f"{BASE_URL}")
    assert res.status_code == 200


def test_local_index_request(session):
    BASE_URL = "http://127.0.0.1:8080"
    res = requests.get(f"{BASE_URL}")
    assert os.getenv("ROBYN_URL") == "127.0.0.1"
    assert res.status_code == 200


def test_global_index_request(global_session):
    host = get_network_host()
    BASE_URL = f"http://{host}:8080"
    res = requests.get(f"{BASE_URL}")
    assert os.getenv("ROBYN_URL") == f"{host}"
    assert res.status_code == 200


def test_dev_index_request(dev_session):
    BASE_URL = "http://127.0.0.1:8081"
    res = requests.get(f"{BASE_URL}")
    assert os.getenv("ROBYN_PORT") == "8081"
    assert res.status_code == 200
