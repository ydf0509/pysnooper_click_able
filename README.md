## 1. pip install pysnooper_click_able

神级别黑科技装饰器。自动显示代码运行轨迹并在pycharm控制台点击可以紧缺跳转到文件的代码行。 

```
基于pysnooper的改版
举要功能是调试debu代码用的，基础用法 百度 pysnooper 就可以。

对比pysnooper
1.增加代码运行轨迹可点击精确跳转
2.根据各种运行状态变彩色
3.增加了代码执行总行数的统计，让程序员心里有谱到底一行调用代码真正背后执行了多少行python代码

```
 
 
 ```python
# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/12/4 0004 17:01
"""
举个例子，统计requests.get运行轨迹，requests和urllib发http请求各执行了多少行代码。

requests请求http百度，会花费18635行代码，requests如果请求https需要执行达到4万多行，性能更是严重下降
urllib 请求百度http ，会花费11902行代码

普通3Ghz以下的电脑，单进程运行python，选一个或者自己做一个流量消耗非常少的http接口进行请求测试，
平均每秒不可能运行超过300次请求。
所以大规模发requests不是简单的io密集型，也是消耗性能的，
包括最牛的英特尔5Ghz的频率，单核如果每秒能运行1000次requests请求，我愿意把电脑cpu吃了。
"""

import requests
import urllib3
from urllib import request
from pysnooper_click_able import snoop
#
# ss = requests.session()
@snoop(depth=100,dont_effect_on_linux=False)
def f():
    # requests.get('http://www.baidu.com')
    # requests.get('http://www.sina.com')
    response = request.urlopen('http://www.baidu.com')
    # ss.get('http://www.baidu.com')


f()
```


## 追踪代码的运行的分支

```python
from pysnooper_click_able import snoop


def f1(x):
    if x == 1:
        a = 2
    else:
        a = 3


def f2(x):
    if x == 7:
        b = 8
        for i in range(1000):
            b += i
    else:
        b = 9


@snoop(depth=9)
def f3(x, test=True):
    if test:
        f1(x)
    else:
        f2(x)


f3(5, False)


```

如果传f(5,False) ,则会显示执行了f2函数，并运行了b=9 的else分支，并显示执行的时间代码行数是8。

![Image text](https://i.niupic.com/images/2020/06/19/8hmF.png)


如果传f(7,False) ,则会显示执行了f2函数，并运行了b=8 的if分支，并显示运行了2009行，

因为  for i in range(1000): 和 b += i 这两行各执行了1000次。

