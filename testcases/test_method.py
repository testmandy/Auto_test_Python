# coding=utf-8
# @Time    : 2019/8/30 10:22
# @Author  : Mandy
import json
import unittest

import requests


class RunMain:
    def __init__(self, method, url, data=None):
        self.res = self.main(method, url, data)

    def get_method(self, url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=2)

    def post_method(self, url, data):
        res = requests.post(url=url, data=data).json()
        return json.dumps(res, indent=2)

    def main(self, method, url, data=None):
        res = None
        if method == "GET":
            res = self.get_method(url, data)
        else:
            res = self.post_method(url, data)
        return res



