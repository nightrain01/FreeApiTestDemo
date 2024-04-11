import os

from util.data.data_reader import DataReader


class BaseDataGetter:

    def __init__(self):
        self.DATA_PATH = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))),
            'data'
        )
        self.dataReader = DataReader()
