import os

import pytest

from util.read_data import *


@pytest.fixture(scope='function')
def fixture_function():
    print('start_fixture_function')
    yield
    print('end_fixture_function')


@pytest.fixture(scope='class')
def fixture_class():
    print('start_fixture_class')
    yield
    print('end_fixture_class')


@pytest.fixture(scope='module')
def fixture_module():
    print('start_fixture_module')
    yield
    print('end_fixture_module')


@pytest.fixture(scope='package')
def fixture_package():
    print('start_fixture_package')
    yield
    print('end_fixture_package')


@pytest.fixture(scope='session')
def fixture_session():
    print('start_fixture_session')
    yield
    print('end_fixture_session')
