import requests
from data import create_user

base_url = 'http://localhost:3000'


class User:

    def createUser(self):
        data = create_user()
        response = requests.post(
            f"{base_url}/auth/register", data=data)

        if (response.status_code == 200 or response.status_code == 201):
            print('\033[92m' + 'User created: ' + data['nickname'] + '\033[0m')
            print(response.json()["access_token"])

        else:
            print('\033[91m' + 'User not created: ' +
                  data['nickname'] + '\033[0m')
            print(response.json())


class Post:
    def __init__(self, data):
        pass
