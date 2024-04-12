import os

from util.data.data_reader import DataReader


class BaseDataGetter:
    """
    基础的数据获取器
    提供一些共通的内容
    """

    def __init__(self):
        self.DATA_PATH = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))),
            'data'
        )
        self.dataReader = DataReader()
