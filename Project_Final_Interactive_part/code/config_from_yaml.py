import os

import yaml
from easydict import EasyDict


def convert_easydict_to_dict(easydict) -> dict:
    the_dict = dict()
    for key, value in easydict.items():
        if hasattr(value, 'items'):
            the_dict.update({key: convert_easydict_to_dict(value)})
        else:
            the_dict.update({key: value})
    return the_dict


def config_from_yaml_file(config_file):
    """
    :param config_file: a yaml config file
    :return: an EasyDict. a dictionary which allows to access dict values as attributes (works recursively).
    """
    with open(config_file, 'r') as stream:
        try:
            _config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return EasyDict(_config)


def get_absolute_path_from_relative_path(path: str):
    string_list = path.split("/")
    project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    if string_list[0] in {"..", "."}:
        string_list[0] = project_dir
        config_path = os.path.join(*string_list)
        return config_path
    else:
        return path


if __name__ == "__main__":
    config = config_from_yaml_file("config.yaml")
    print("config is ", config)