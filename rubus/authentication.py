import getpass
import json
import os

import click
import requests


def create_headers() -> dict:
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + os.environ['RUBUS_SESSION']
        }
        return headers
    except Exception:
        click.echo(
            'Please, log in and set the RUBUS_SESSION environment variable before using this command.')
        os.sys.exit(0)


def handle_response(expected_status_code: int, r):
    click.echo('\n')
    if r.status_code != expected_status_code:
        click.echo(r.json()['error'])
    else:
        click.echo(json.dumps(r.json(), indent=4, sort_keys=True))


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
    except requests.ConnectionError:
        click.echo('Server is not responding, please try again later.')
    except Exception as e:
        print(e)
        click.echo('Error, wrong username or password.\n')


def info(baseUrl: str):
    headers = create_headers()
    try:
        r = requests.get(baseUrl + '/user/me', headers=headers)
        handle_response(200, r)
    except requests.ConnectionError:
        click.echo('Server is not responding, please try again later.')


def update(baseUrl: str):
    headers = create_headers()
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

    try:
        r = requests.put(baseUrl + '/user/me',
                         headers=headers, data=json.dumps(user))
        handle_response(200, r)
    except requests.ConnectionError:
        click.echo('Server is not responding, please try again later.')
