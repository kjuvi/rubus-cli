import getpass
import rubus.http as http
import requests


def create_user(config):
    user = {}
    user['username'] = input('Enter a username for the new user: ')
    user['email'] = input('Enter an email for the new user: ')
    user['password'] = getpass.getpass('Enter a password for the new user: ')
    answer = input('Should I give administrative rights to this user ? [y/N] ')
    user['role'] = 'administrator' if answer == 'y' or answer == 'Y' else 'user'

    r = requests.post(config.baseURL + '/admin/user', headers=config.headers,
                      json=user)
    http.handle_response(201, r)


def add_device(config):
    hostname = input('Enter the device\'s hostname: ')
    port = input('Enter the device\'s port: ')

    params = {'hostname': hostname, 'port': port}
    r = requests.post(config.baseURL + '/admin/device',
                      params=params, headers=config.headers)
    http.handle_response(201, r)


def delete_device(config):
    hostname = input('Enter the device\'s hostname: ')
    device_id = input('Enter the device\'s id: ')

    params = {'hostname': hostname, 'deviceId': device_id}
    r = requests.delete(config.baseURL + '/admin/device',
                        params=params, headers=config.headers)
    http.handle_no_content('Device has been deleted.', r)
