## 简介

## 项目结构说明
### data：数据驱动地址
### testing：测试用例目录
+   test_calc.py 计算器测试用例
### util：封装常用工具
+   conftest.py 定义fixture
    +   func 测试用例的setup和teardown，级别作用于模块
+   readyaml.py --读取yaml文件的数据
    +   yaml_data(filepath) --接收数据(传入yaml文件路径)
    +   yaml_data_key(key)  --根据key获取yaml文件的数据


## 参考链接

## 说明
> 使用 pytest 解释器执行，并且加上打印详细日志的参数 -v 就会显示PASS， 否则 就会简写，. 点代表 PASS,   F代表 fail 