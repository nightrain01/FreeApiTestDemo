import yaml


class DataReader:
    """
    数据读取器
    将来可以支持多种不同类型数据的读取
    """

    def read_yaml_data(self, path):
        """
        读取yaml文件
        :param path: yaml文件路径
        :return: yaml文件的dict形式
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            return data
        except Exception as e:
            print(e)
