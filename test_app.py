# test_app.py
import app

def test_home():
    response = app.app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello from docker on Gitpod" in response.data
