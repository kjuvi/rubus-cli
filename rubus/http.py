import json
import os

import click


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


def handle_no_content(message: str, r):
    click.echo('\n')
    if r.status_code != 204:
        click.echo(r.json()['error'])
    else:
        click.echo(message)
