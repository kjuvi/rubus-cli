import click
import rubus.http as http
import requests


def add(config):
    hostname = input('Enter the device\'s hostname: ')
    port = input('Enter the device\'s port: ')

    params = {'hostname': hostname, 'port': port}
    r = requests.post(config.baseURL + 'add',
                      params=params, headers=config.headers)
    http.handle_response(201, r)


def delete(config):
    hostname = input('Enter the device\'s hostname: ')
    device_id = input('Enter the device\'s id: ')

    params = {'hostname': hostname}
    r = requests.post(config.baseURL + device_id + '/delete',
                      params=params, headers=config.headers)
    if r.status_code == 204:
        click.echo('Device has been deleted.')
    else:
        click.echo(r.json())


def list(config):
    r = requests.get(config.baseURL, headers=config.headers)
    http.handle_response(200, r)


def get(config, device_id):
    r = requests.get(config.baseURL + device_id, headers=config.headers)
    http.handle_response(200, r)


def acquire(config, device_id):
    r = requests.post(config.baseURL + device_id + '/acquire',
                      headers=config.headers)
    http.handle_response(200, r)


def release(config, device_id):
    r = requests.post(config.baseURL + device_id + '/release',
                      headers=config.headers)
    http.handle_response(200, r)


def deploy(config, device_id):
    r = requests.post(config.baseURL + device_id + '/deploy',
                      headers=config.headers)
    if r.status_code == 204:
        click.echo('Device deployed.')
    else:
        click.echo(r.status_code)


def on(config, device_id):
    r = requests.post(config.baseURL + device_id +
                      '/on', headers=config.headers)
    if r.status_code == 204:
        click.echo('Device is on.')
    else:
        click.echo(r.status_code)


def off(config, device_id):
    r = requests.post(config.baseURL + device_id +
                      '/off', headers=config.headers)
    if r.status_code == 204:
        click.echo('Device is off.')
    else:
        click.echo(r.status_code)
