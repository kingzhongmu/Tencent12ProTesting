## 介绍
pytest自动化项目演示

##  markdown语法：
https://markdown.com.cn/basic-syntax/

## pycharm中设置使用pytest
Mac下
Settings-->Tools-->Python Integrated Tools， 把Default test runner换为pytest就可以了

## pytest测试用例识别
##### 测试文件：  
》  test_*.py \
》  \*_test.py 
##### 识别用例：  
》  Test*类中包含的所有test_*的方法（测试类不能有__init__方法） \
》  不在class中的所有的test_*方法 
##### pytest也可以执行unittest框架写的用例和方法

## pytest执行

##### 在pycharm的py文件上直接运行（前提条件是配置了pytest运行）

##### Terminal上运行

pytest -h   -- 打印帮助信息 \
pytest xx.py   --直接运行,会搜索当前文件内所有可运行内容 \
pytest -v -s xx.py   -- -v是打印详细运行日志 -s是带控制台输出结果 \
pytest -v -s xx.py::类名  -- 运行模块的某个类 \
pytest -v -s xx.py::类名::方法  -- 运行模块中的某个类的某个方法 \
pytest -v -k "类名 and not 方法名"  -- 跳过某个方法，如果没有not，就是只运行某个方法 \
示例：pytest -v -k "TestCalc and not test_add_1" \
pytest -v -m "标记名"  -- 只运行有这个标记的用例 @pytest.mark.标记名 \
pytest -x 文件名  -- 一旦运行到报错就停止运行 \
pytest --maxfail=3  -- 当运行错误达到3次的收停止运行 \


## pytest的参数化
格式：@pytest.mark.parametrize(para1, para2) \
    para1: 要参数化的变量；字符串（逗号分隔），list，元祖 \
    para2: 要参数化变量的值；list，元祖  \
示例：@pytest.mark.parametrize('data1, data2, expect', yaml.safe_load(open('datas/add1.yml'))) \
    注意，yaml读出来的对象一定要是一个list


## pytest插件包

##### 1运行失败后重新运行：pytest-rerunfailures
pip install pytest-rerunfailures \
pytest -v -s --reruns 3 test_xx.py   -- 测试失败后重新运行3次 \
pytest -v --reruns 5 --reruns-delay 1  -- 失败后每次运行等待1s 

##### 2断言失败后仍会继续执行：pytest-pytest-assume
pip install pytest-assume 一个方法中写多条断言，
即使前面的断言执行失败也会暂停执行，仍会继续执行下去，但是用例还是会执行失败
程序中直接使用： pytest.assume(3 == 2) 代替assert(3 == 2)

##### 3断言失败后仍会继续执行：pytest-pytest-assume




# 备用知识：
yaml入门：https://www.runoob.com/w3cnote/yaml-intro.html