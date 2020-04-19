import click

import rubus.authentication as auth


class Config(object):

    def __init__(self):
        self.verbose = False
        self.baseURL = 'http://pi-controller:8080/v1'


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@pass_config
def cli(config, verbose):
    config.verbose = verbose


@cli.command()
@click.option('--info', is_flag=True, help='Display the user\'s credentials.')
@click.option('--login', is_flag=True, help='Log in to receive a token for your session.')
@click.option('--update', is_flag=True, help='Update your credentials.')
@pass_config
def authentication(config, info, login, update):
    if info:
        auth.info(config.baseURL)
    elif login:
        auth.login(config.baseURL)
    elif update:
        auth.update(config.baseURL)
