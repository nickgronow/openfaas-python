from typing import Union
import os
from flask import request


class Event:
    '''
    Class containing data from the request
    '''
    body: Union[dict, str]
    headers: dict
    method: str
    query: dict
    path: str

    def __init__(self):
        if request.is_json:
            self.body = request.get_json()
        else:
            self.body = request.get_data()
        self.headers = request.headers
        self.method = request.method
        self.query = request.args
        self.path = request.path


class Context:
    '''
    Contains context data, such as hostname
    '''
    hostname: str

    def __init__(self):
        self.hostname = os.environ['HOSTNAME']


