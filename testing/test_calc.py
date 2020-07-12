#!/usr/bin/emv python
# -*- coding: utf-8 -*-
import pytest
import allure
from util.readyaml import yaml_data_key
from pythoncode.calc import Calculator
from util.conftest import func


@pytest.mark.usefixtures("func")
class TestClac():



    # @pytest.mark.parametrize("a,b",[
    #     (1,1)
    # ])
    @pytest.mark.add
    @pytest.mark.parametrize('a,b,c', yaml_data_key('add'),ids = ['int','int','int','float','fushu'])
    #@pytest.mark.parametrize('a,b,c',[[1,1,2],[2,2,4]])
    @allure.story("加法")
    def test_add(self,a,b,c):
        """
        加法测试用例
        :param a:
        :param b:
        :param c:
        :return:
        """
        cal = Calculator()
        print(f'\na,b,c的值:{a} + {b} = {c}')
        assert cal.add(a,b) == c

    @pytest.mark.sub
    @pytest.mark.parametrize('a,b,c', yaml_data_key('sub'),ids = ['int','int','int','float','fushu'])
    @allure.story("减法")
    def test_sub(self,a,b,c):
        """
        减法测试用例
        :param a:
        :param b:
        :param c:
        :return:
        """
        cal = Calculator()
        print(f'\na,b,c的值:{a} - {b} = {c}')
        assert cal.sub(a,b) == c

    @pytest.mark.mul
    @pytest.mark.parametrize('a,b,c', yaml_data_key('mul'),ids = ['int','int','int','float','fushu'])
    @allure.story("乘法")
    def test_mul(self,a,b,c):
        """
        乘法测试用例
        ((Decimal(a) * Decimal(b)).quantize(Decimal('0.00'))
        :param a:
        :param b:
        :param c:
        :return:
        """
        import decimal
        cal = Calculator()
        print(f'\na,b,c的值:{a} * {b} = {c}')
        assert cal.mul(a,b) == c

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,c', yaml_data_key('div'),ids = ['int','int','int','int','float','fushu'])
    @allure.story("除法")
    def test_div(self,a,b,c):
        """
        除法测试用例
        :param a:
        :param b:
        :param c:
        :return:
        """
        with allure.step("实例化"):
            cal = Calculator()
        with allure.step("判断除数是否为0"):
            if b != 0:
                print(f'\na,b,c的值:{a} / {b} = {c}')
                assert cal.div(a,b) == c
            else:
                allure.attach("<body>这是一段html body块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)
                allure.attach.file("../report/photo/a.jpg", name="这是图片", attachment_type=allure.attachment_type.JPG)
                allure.attach("除数不能为0！", attachment_type=allure.attachment_type.TEXT)
                print("除数不能为0！")


