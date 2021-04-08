# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/12/4 0004 17:01
"""
举个例子，统计requests.get运行轨迹，requests和urllib发http请求各执行了多少行代码。

requests请求http百度，会花费18635行代码
urllib 请求百度http ，会花费11902行代码

普通3Ghz以下的电脑，单进程运行python，选一个流量消耗非常少的接口，平均每秒不可能运行超过300次请求。
所以大规模发requests不是简单的io密集型，也是消耗性能的，
包括最牛的英特尔5Ghz的频率，如果每秒能运行1000次requests请求，我愿意把电脑cpu吃了。
"""

import requests
import urllib3
from urllib import request
from pysnooper_click_able import snoop
# from pysnooper042 import snoop
import logging
import asyncio
import aiohttp
#
import nb_log


@snoop(depth=1000,dont_effect_on_linux=True)
def f():
    # ss = requests.session()
    # ss = urllib3.PoolManager()
    # resp = ss.request('get','https://www.v2ex.com/amp/t/575411')
    # requests.get('http://www.sina.com')
    # response = request.urlopen('https://www.baidu.com')
    # ss.get('http://www.baidu.com')

    # logging.getLogger('hi').warning('helo')
    for i in range(1):
        nb_log.simple_logger.warning('haha')


# @snoop(depth=1000,)
async def af():
        # with snoop(depth=100):
        async with aiohttp.request('get', url='https://www.baidu.com') as resp:
            text = await resp.text()
            print(text)


if __name__ == '__main__':
    f()
    # asyncio.get_event_loop().run_until_complete(af())
