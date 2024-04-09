import os

from util.read_data import *

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
parametrize_data = read_yaml_data(os.path.join(BASE_PATH, 'data', 'test_parametrize_data.yml'))
# parametrize_data = read_yaml_data('./data/test_parametrize_data.yml')
