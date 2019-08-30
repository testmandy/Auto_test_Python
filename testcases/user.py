# coding=utf-8
# @Time    : 2019/8/30 12:55
# @Author  : Mandy
import json
import unittest

from testcases.test_method import RunMain


class User(unittest.TestCase):

    def test_get_status(self):
        # url = "https://translate.google.cn/"
        url = "http://54.241.21.249:8089/skyvpn/advpStatus/get?userId=7393118869590990&country=CN&" \
              "deviceId=iOS.0de30616a8b151ac12aedc44e80901b6.skyvpn&token=64f0338187b6ae61adeeb6c608246ab4"
        run = RunMain('GET', url, None)
        result = json.loads(run.res)
        print(result['result'])
        self.assertEqual(result['result'], 1, '获取状态失败')


unittest.main()
