# coding=utf-8
# @Time    : 2019/8/30 12:27
# @Author  : Mandy
#!/usr/bin/env python
# coding=utf-8
import os

import pytest
import allure
import yaml


project_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(project_dir, 'logs\\')
report_dir = os.path.join(project_dir, 'report\\')
case_dir = os.path.join(project_dir, 'testcases\\')
case_method_dir = os.path.join(project_dir, 'testcases\\test_method.py')
sheet_dir = os.path.join(project_dir, 'testFile\\testcases.xls')


@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    Parse env config info
    """
    root_dir = request.config.rootdir
    config_path = '{0}/config/env_config.yml'.format(root_dir)
    with open(config_path) as f:
        env_config = yaml.load(f) # 读取配置文件

    allure.environment(host=env_config['host']['domain']) # 测试报告中展示host
    allure.environment(browser=env_config['host']['browser']) # 测试报告中展示browser

    return env_config
