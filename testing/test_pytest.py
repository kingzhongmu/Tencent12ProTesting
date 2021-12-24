#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import pytest
import sys
from decimal import Decimal
from python.calc import Calc

sys.path.append("..")


def steps():
    with open("datas/steps.yml") as f:
        return yaml.safe_load(f)


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_fail(self):
        print("--- 计数")
        assert 3 == 2

    # mark标记为 demo 和 second
    # @pytest.mark.demo
    # @pytest.mark.second
    def test_add(self):
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result

    # @pytest.mark.run(order=-1)
    def test_div(self):
        result = self.calc.div(2, 2)
        assert 1 == result

    @pytest.mark.parametrize('data1, data2, expect',
                             yaml.safe_load(open('datas/add1.yml')))
    def test_add_1(self, data1, data2, expect):
        steps1 = steps()
        for step in steps1:
            print(f"step ==== > {step}")
            if 'add' == step:
                result = self.calc.add(data1, data2)
            elif 'add1' == step:
                result = self.calc.add1(data1, data2)
            print(result)
            assert expect == result


        # result = self.calc.add(data1, data2)
        # print(result)
        # assert expect == result
        #
        # result1 = self.calc.add1(data1, data2)
        # print(result1)
        # assert expect == result1

class TestCalc2:
    def setup(self):
        self.calc = Calc()

    def test_div_x(self):
        result = self.calc.div(2, 2)
        assert 1 == result

if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest.py::TestCalc::test_div'])
