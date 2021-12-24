#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import pytest
import sys
from decimal import Decimal
from python.calc import Calc

sys.path.append("..")

# 默认的scope的参数是function，只能在方法中可用
@pytest.fixture()
def login():
    print("\nI haved loged in !")

# scope的默认值是function，默认只在函数上可用
# 这里指定module，指定在模块中可用
# 注意：在出现open_browser的位置第一次调用，在整个模块用例执行完之后第二次调用
# 【感觉有点鸡肋，因为放到 setup好像也可以】
@pytest.fixture(scope="module")
def open_browser():
    print("\n 打开浏览器")
    yield
    print("最后关闭浏览器")


# autouse=True后，默认会在每个测试用例执行前都会执行这个语句
@pytest.fixture(autouse=True)
def open_browser():
    print("\n打开浏览器的cookie")


test_data = ['tom', 'jerry']
# 方法名作为参数，传入到用例中；同时方法func_name_as_para的参数也作为参数传入parametrize中
# 名字不能瞎起呀，之前用过测试用例后办部分的名字func_name_as_para，会报错
@pytest.fixture(scope="module")
def login_r(request):
    print("登录的用户是：", request)


# @pytest.fixture(autouse=True) 还可以卸载conftest.py中

def steps():
    with open("datas/steps.yml") as f:
        return yaml.safe_load(f)


class TestCalc():
    def setup(self):
        self.calc = Calc()

    def test_fail(self):
        print("--- 计数")
        assert 3 == 2

    # 要安装 pip install pytest-assume 一个方法中写多条断言，
    # 即使前面的断言执行失败也会继续执行下去，但是结果还是按照失败处理
    def test_pytest_assume(self):
        pytest.assume(3 == 2)
        print("\n--- test test_pytest_assume")
        assert True

    # mark标记为 demo 和 second
    # pytest -v -m "标记名"  -- 只运行有这个标记的用例 @pytest.mark.标记名
    # pytest -v -m "not 标记名"  -- 不执行哪些标记的用例
    @pytest.mark.demo
    def test_mark(self):
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result

    # 传入的login被@pytest.fixture()修饰
    def test_fixture(self, login):
        print("我是test_fixture用例")
        assert True

    # 测试scope范围为module
    def test_fixture_scope(selfs, open_browser):
        print("我是test_fixture_scope")
        assert True

    # @pytest.mark.run(order=-1)
    def test_div(self):
        result = self.calc.div(2, 2)
        assert 1 == result

    # 测试传入外界参数的方式执行测试用例
    @pytest.mark.parametrize('data1, data2, expect',[[1, 2, 3], [10, 20, 30]])
    def test_mark_parametrize(self, data1, data2, expect):
        steps1 = steps()
        for step in steps1:
            print(f"step ==== > {step}")
            if 'add' == step:
                result = self.calc.add(data1, data2)
            elif 'add1' == step:
                result = self.calc.add1(data1, data2)
            print(result)
            assert expect == result

    # 测试传入外界参数【从文件中读取】的方式执行测试用例
    @pytest.mark.parametrize('data1, data2, expect',
                             yaml.safe_load(open('datas/add1.yml')))
    def test_mark_parametrize_out_data(self, data1, data2, expect):
        steps1 = steps()
        for step in steps1:
            print(f"step ==== > {step}")
            if 'add' == step:
                result = self.calc.add(data1, data2)
            elif 'add1' == step:
                result = self.calc.add1(data1, data2)
            print(result)
            assert expect == result

    # 测试参数组合的方式执行用例
    @pytest.mark.parametrize('data1',(1, 2, 3))
    @pytest.mark.parametrize('data2', (5, 10, 11))
    def test_mark_parametrize_com(self, data1, data2):
        print("data1 + data2: ", data1 + data2)
        assert True

    # 方法名做为参数传入到parametrize
    @pytest.mark.parametrize("login_r", test_data, indirect=True)
    def test_mark_parametrize_func_name_as_para(self, login_r):
        print("test_mark_parametrize_func_name_as_para")
        assert True

    # 测试mark的skip和skipif用法
    @pytest.mark.skip("此次测试不执行这条用例")
    def test_mark_skip(self):
        print("执行用例test_mark_skip")
        assert True

    @pytest.mark.skipif(sys.platform=="win32", reason="不在win32上运行这个用例")
    def test_mark_skipif(self):
        print("执行用例test_mark_skipif")
        assert True

    # 预先标注为fail【程序有些预留的问题，执行结果待考虑】
    @pytest.mark.xfail
    def test_mark_xfail(self):
        print("执行用例test_mark_xfail")
        assert True
        assert False

    # 多个cpu分布式执行测试用例，安装pip install pytest-xdist
    # 执行时加上 -n 3   3 是并行的cpu个数

    # 生成测试报告  pip install pytest-html
    # 执行时加上 --html=report.html --self-contained-html


class TestCalc2:
    def setup(self):
        self.calc = Calc()

    def test_div_x(self):
        result = self.calc.div(2, 2)
        assert 1 == result

if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest.py::TestCalc'])
