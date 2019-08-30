# coding=utf-8
# @Time    : 2019/8/30 9:26
# @Author  : Mandy
import os

import conftest

os.system("pytest -v " + conftest.case_method_dir)
