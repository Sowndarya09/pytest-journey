import requests

def test_get_user():
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    assert response.status_code == 200

    body = response.json()
    assert body['id'] == 1
    assert body['username']!= ''
    assert '@' in body['email']



def test_create_user():
    response = requests.post('https://jsonplaceholder.typicode.com/users', 
        json={
            'name': 'Sownd',
            'email': 'sownd@gmail.com',
            'username': 'sragu'
        })
    
    assert response.status_code == 201
    body = response.json()
    assert body['name'] == 'Sownd'


def test_update_user():
    response = requests.put('https://jsonplaceholder.typicode.com/users/1', 
        json={
            'name': 'Sowndarya',
            'email': 'sownd@gmail.com',
            'username': 'sragu'
        })
    
    assert response.status_code == 200
    body = response.json()
    assert body['name'] == 'Sowndarya'

def test_delete_user():
    response = requests.delete('https://jsonplaceholder.typicode.com/users/1')
    # Note: jsonplaceholder returns 200 for DELETE
    # In production APIs this should be 204 No Content
    assert response.status_code == 200
    

