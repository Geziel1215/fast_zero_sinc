from http import HTTPStatus

# def teste_read_root_deve_retornar_ok_e_ola_mundo():
#     client = TestClient(app)

#     response = client.get('/')

#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'Ola Mundo'}


def teste_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'gesiel',
            'password': '123456',
            'email': 'gesiel@hotmail.com.br',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'gesiel',
        'email': 'gesiel@hotmail.com.br',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'gesiel',
                'email': 'gesiel@hotmail.com.br',
                'id': 1,
            }
        ]
    }
