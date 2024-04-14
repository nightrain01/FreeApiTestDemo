import os

from data.data_getters.base_data_getter import BaseDataGetter


class FreeApiDataGetter(BaseDataGetter):
    """
    免费Api测试数据获取器
    """

    def __init__(self):
        super().__init__()

    def get_free_api_group0_data(self):
        """
        获取第0组免费Api的测试数据
        :return: dict形式的测试数据
        """
        yaml_data_path = os.path.join(self.DATA_PATH, 'free_api_group0_test_data.yml')
        try:
            parametrize_data = self.dataReader.read_yaml_data(yaml_data_path)
            return parametrize_data
        except Exception as e:
            print(e)

    def get_ruoyi_vue_data(self):
        """
        获取Ruoyi-Vue测试数据
        :return:
        """
        yaml_data_path = os.path.join(self.DATA_PATH, 'ruoyi_vue_test_data.yml')
        try:
            parametrize_data = self.dataReader.read_yaml_data(yaml_data_path)
            return parametrize_data
        except Exception as e:
            print(e)
