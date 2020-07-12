#！/usr/bin/env python
# -*- encoding=utf-8 -*-
import pytest

@pytest.fixture(scope="module",autouse=True)
def func():
    """
    计算器测试用例初始化setup和teardown
    :return:
    """
    print("【开始计算】")

    yield

    print("【计算结束】")

