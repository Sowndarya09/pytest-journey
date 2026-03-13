import requests

def test_get_user():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    assert response.status_code == 200

    body = response.json()
    assert body['id'] == 1
    assert body['username']!= ''
    assert '@' in body['email']
