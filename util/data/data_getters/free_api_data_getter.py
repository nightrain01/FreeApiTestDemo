import os

from util.data.data_getters.base_data_getter import BaseDataGetter


class FreeApiDataGetter(BaseDataGetter):
    def __init__(self):
        super().__init__()

    def get_free_api_group0_data(self):
        yaml_data_path = os.path.join(self.DATA_PATH, 'free_api_group0_test_data.yml')
        try:
            parametrize_data = self.dataReader.read_yaml_data(yaml_data_path)
            return parametrize_data
        except Exception as e:
            print(e)
