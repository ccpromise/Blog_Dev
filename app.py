# This script runs on servier to respond http request in asynchronized mode

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

@asyncio.coroutine
def index(request): 
	# This is a REQUEST HANDLER which accepts a Request instance and returns a Response instance 
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='UTF-8')

# Decorator to mark generator-based coroutines.Able to use yield from to call other coroutines.
@asyncio.coroutine
def init(loop):
	# create an Application instance and register the request handler with router on a particular HTTP method and path
    app = web.Application(loop=loop) # event loop used for HTTP request. For all the http requests, push it into event loop so that multiple http requests could be responded without waiting for one request to finish
    app.router.add_route('GET', '/', index)
    # yield from: suspends the coroutine until the future is done
    # create a TCP server bound to a host and port
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop() # create a message loop for asynchronized IO
loop.run_until_complete(init(loop))
loop.run_forever()