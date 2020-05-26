# Rubus Client

This project contains a command-line interface program to interact
with a deployed instance of [rubus-api](https://github.com/kjuvi/rubus-api).


## Commands overview

All the commands are grouped by functionalities. Here is a quick overview of
how they are structured:

- **rubus**
    - **admin**: these commands require administrative rights
    - **authentication**: Log in and manage your user
    - **device**: manage devices (turn on/off, deployment, ...)


## Configuring the server

By default, Rubus will try to reach a running instance of Rubus API on
localhost. You can configure another address with the `RUBUS_API_URL`
environment variable.

## Authentication system

Excepted for the login, all the other commands require to be authenticated.
Rubus API works with JWT and will return you one on a successful login. Since
Rubus CLI is quite minimalist, there is no persistence, and you will have to
take advantage of your shell capabilities.

In other words, Rubus CLI will display the JWT, and prompt you to save it as an
environment variable (i.e. `RUBUS_SESSION`). The token is valid as long as your
user has not reach his expiration time (if any).

You can either set it once and for good, for example in your `.bashrc`, or just
set it in your current shell. Closing the shell will operate as a log out.
However, keep in mind that it may be accessible through the `bash_history`, in
case you are on a public computer.

