import getpass
import rubus.http as http

import click
import requests


def login(baseURL: str):
    username = input("Username: ")
    password = getpass.getpass('Password: ')
    payload = {'username': username, 'password': password}
    try:
        r = requests.get(baseURL + '/user/login', params=payload)
        token = r.json()['token']
        click.echo(
            f'''You are logged in!

In order to perform any other command, set your session key to the
`RUBUS_SESSION` environment variable. ex:

$ export RUBUS_SESSION={token}

            ''')
    except Exception as e:
        print(e)
        click.echo('Error, wrong username or password.\n')


def info(config):
    r = requests.get(config.baseURL + '/user/me', headers=config.headers)
    http.handle_response(200, r)


def update(config):
    user = {}

    answer = input('Do you want to update your username? [y/N] ')
    if answer == 'y' or answer == 'Y':
        user['username'] = input('Enter a new Username: ')

    answer = input('Do you want to update your email? [y/N] ')
    if answer == 'y' or answer == 'Y':
        user['email'] = input('Enter a new Email: ')

    answer = input('Do you want to update your password? [y/N] ')
    if answer == 'y' or answer == 'Y':
        user['password'] = getpass.getpass('Enter a new Password: ')

    r = requests.put(config.baseURL + '/user/me',
                     headers=config.headers, json=user)

    http.handle_response(200, r)
