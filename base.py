import os
from database import Database
import logging
from typing import Union


class Event:
    """
    Class containing data from the request
    """

    body: Union[dict, str]
    headers: dict
    method: str
    query: dict
    path: str


class Context:
    """
    Contains context data, such as hostname
    """

    hostname: str


def db() -> Database:
    namespace = os.environ.get("APP_NAME")
    return Database(
        host=secret("wov-db-host"),
        database=secret(f"{namespace}-db-name"),
        user=secret(f"{namespace}-db-user"),
        password=secret(f"{namespace}-db-pw"),
    )


def secret(name: str) -> str:
    path = os.environ.get("secrets") or "/var/openfaas/secrets"
    fullpath = f"{path}/{name}"
    with open(fullpath, "r") as file:
        return file.read().rstrip("\n")


def log(message: str) -> str:
    if testing():
        return
    logging.info(message)


def testing() -> bool:
    return os.environ.get("TESTING")


def production() -> bool:
    return os.environ.get("APP_ENV") == "production"


def response(payload: dict, code=200):
    return {
        "body": payload,
        "headers": {"content-type": "application/json"},
        "code": code,
    }
