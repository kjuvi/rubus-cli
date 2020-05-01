import rubus.http as http
import requests


def list(config):
    r = requests.get(config.baseURL + '/device', headers=config.headers)
    http.handle_response(200, r)


def get(config, device_id):
    r = requests.get(config.baseURL + '/device/' + device_id, headers=config.headers)
    http.handle_response(200, r)


def acquire(config, device_id):
    r = requests.post(config.baseURL + '/device/' + device_id + '/acquire',
                      headers=config.headers)
    http.handle_response(200, r)


def release(config, device_id):
    r = requests.post(config.baseURL + '/device/' + device_id + '/release',
                      headers=config.headers)
    http.handle_response(200, r)


def deploy(config, device_id):
    r = requests.post(config.baseURL + '/device/' + device_id + '/deploy',
                      headers=config.headers)
    http.handle_no_content('Device deployed.', r)


def on(config, device_id):
    r = requests.post(config.baseURL + '/device/' + device_id +
                      '/on', headers=config.headers)
    http.handle_no_content('Device is on.', r)


def off(config, device_id):
    r = requests.post(config.baseURL + '/device/' + device_id +
                      '/off', headers=config.headers)
    http.handle_no_content('Device is off.', r)
