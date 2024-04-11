import os

from util.data.data_reader import DataReader


class LearningDataGetter:
    def __init__(self):
        self.DATA_PATH = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))),
            'data'
        )
        self.dataReader = DataReader()

    def get_parametrize_data(self):
        yaml_data_path = os.path.join(self.DATA_PATH, 'learning_test_data.yml')
        try:
            parametrize_data = self.dataReader.read_yaml_data(yaml_data_path)
            return parametrize_data
        except Exception as e:
            print(e)
