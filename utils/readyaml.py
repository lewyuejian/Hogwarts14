#！/usr/bin/env python
# -*- encoding=utf-8 -*-
import yaml


#https://ceshiren.com/t/topic/3467


def yaml_data(filepath):
    """
    定义获取yaml文件数据
    :param filepath:
    :return:
    """
    with open(filepath,encoding='utf-8') as f:
        return yaml.safe_load(f)

def yaml_data_key(key):
    """
    根据key获取数据
    :param key:
    :return:
    """
    return yaml_data("../data/calc_data.yaml")[key]


