#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/24 下午2:13
# @Author  : zhiang
# @Site    : 
# @File    : app.py
# @Software: PyCharm

import logging;logging.basicConfig(level=logging.INFO)
import  asyncio, os, json, time
from  datetime import  datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',8082)
    logging.info('server started at http://127.0.0.1:8082...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

