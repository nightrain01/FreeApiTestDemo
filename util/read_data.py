import yaml


def read_yaml_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


if __name__ == '__main__':
    print(read_yaml_data('../data/test_parametrize_data.yml'))