import re

import allure
import pytest


@pytest.fixture(scope='function')
def get_testcase_params(request):
    """
    获取测试运行时的参数
    """
    return request.node.callspec.params


@pytest.fixture(scope='function', autouse=True)
def allure_parameters_filter(get_testcase_params):
    """
    过滤掉testcase_*，expect_*一类的参数
    """
    # yield
    pattern = r'^(testcase_|expect_|issue_)(.+)'
    for key, value in get_testcase_params.items():
        if re.match(pattern, key):
            mode = allure.parameter_mode.HIDDEN
        else:
            mode = allure.parameter_mode.DEFAULT
        allure.dynamic.parameter(name=key, value=value, mode=mode)


@pytest.fixture(scope='function', autouse=True)
def set_allure_title(get_testcase_params):
    """
    为测试用例自动添加allure标题
    """
    yield
    if 'testcase_title' in get_testcase_params and get_testcase_params['testcase_title'] is not None:
        allure.dynamic.title(get_testcase_params['testcase_title'])


@pytest.fixture(scope='function', autouse=True)
def set_allure_description(get_testcase_params):
    """
    为测试用例自动添加allure描述
    """
    yield
    if 'testcase_description' in get_testcase_params and get_testcase_params['testcase_description'] is not None:
        allure.dynamic.description(get_testcase_params['testcase_description'])


@pytest.fixture(scope='function', autouse=True)
def set_allure_issue(get_testcase_params):
    """
    为测试用例自动添加allure issue
    """
    yield
    if 'issue_name' in get_testcase_params and get_testcase_params['issue_name'] is not None \
            and 'issue_url' in get_testcase_params and get_testcase_params['issue_url'] is not None:
        allure.dynamic.issue(get_testcase_params['issue_url'], get_testcase_params['issue_name'])
