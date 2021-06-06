# @name:    DorkScanner
# @repo:    https://github.com/nithin-jaikar/dorkscanner
# @author:  Nithin Jaikar
"""
MIT License

Copyright (c) 2020 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


import asyncio
from proxybroker import Broker
from termcolor import colored, cprint
import sys
import os

B = """
 ____
|  _ \ _ __ _____  ___   _
| |_) | '__/ _ \ \/ / | | |    
|  __/| | | (_) >  <| |_| |    
|_|   |_|  \___/_/\_\\__,  |   
                     |___/
"""
print(B)
print ("")
print(colored('[+] This will find 25 Different working Proxy server Each time :', 'green')) 
print(colored('[+] Starting...', 'green' ))

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print('Found proxy: %s' % proxy)


proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], limit=100 ), show(proxies)
)

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
print(colored('[+] Done', 'green'))

