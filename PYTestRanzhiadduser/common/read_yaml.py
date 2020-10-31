import yaml

from common.readini import Get_ini_data


def read_yaml_data():
    yamlfile = Get_ini_data().get_adduser_yaml_path()
    with open(yamlfile, 'r', encoding='utf8') as fp:
        return yaml.safe_load(fp)
