import os
from pprint import pprint

import yaml


class DataReader:
    @staticmethod
    def read_yaml_data(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            return data
        except Exception as e:
            print(e)


class DataGetter:
    DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data')
    dataReader = DataReader()

    @classmethod
    def get_parametrize_data(cls):
        yaml_data_path = os.path.join(cls.DATA_PATH, 'test_parametrize_data.yml')
        try:
            parametrize_data = cls.dataReader.read_yaml_data(yaml_data_path)
            return parametrize_data
        except Exception as e:
            print(e)


if __name__ == '__main__':
    pprint(DataGetter.get_parametrize_data())
