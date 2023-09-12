import http.client
import requests
import sys
import os

config_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(config_folder_path)
import config


def test_get_flights():
    # arrange
    project_url = config.config.get("apiProjectUrl", "")

    # act
    resp = requests.get(url=project_url)

    # assert http status
    assert resp.status_code == http.client.OK

    # assert response body
    resp_body = resp.json()
    for flight in resp_body['data']:
        assert all(
            [
                isinstance(flight['id'], int),
                flight['id'] is not None ,
                isinstance(flight['from'], str),
                flight['from'] is not None,
                isinstance(flight['to'], str),
                flight['to'] is not None,
                isinstance(flight['date'], str),
                flight['date'] is not None
            ]
        )

    # assert content type
    resp_content_type = resp.headers.get('Content-Type')
    assert resp_content_type == 'application/json'
