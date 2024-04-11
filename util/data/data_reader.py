import yaml


class DataReader:
    def read_yaml_data(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            return data
        except Exception as e:
            print(e)
