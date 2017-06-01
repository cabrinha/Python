'''
Every 2 seconds, print a pair of metric lines with the following formats:

marketdata.latency <unix_timestamp> <value (in seconds)> type=quote
marketdata.latency <unix_timestamp> <value (in seconds)> type=request

Sample output:
marketdata.latency 1493409709 6.143643 type=quote
marketdata.latency 1493409709 0.336949 type=request

In the above lines, the <unix_timestamp> is the unix epoch time at which we are printing the lines (e.g. 1493409709).

In the first line, the <value> refers to the "quote latency", which represents how stale a particular quote is.
To derive this value, we will hit the API endpoint https://api.robinhood.com/quotes/SPY/ (you can open this in a browser or curl this endpoint to see the response).
The response will be a JSON object containing multiple keys, one of which is the "updated_at" time string for the quote.
The quote latency value will be current time minus this "updated_at" time.

In the second line, the <value> refers to the "request latency", which is simply the amount of time it took for the API request/response cycle to complete.
To compute this, we can simply store the times from before and after the request is made, and compute the difference.
'''

import datetime
import requests
import threading
import time


def ticker(stock):
    time.sleep(2)
    start = time.time()
    r = requests.get('https://api.robinhood.com/quotes/{}/'.format(stock)).json()
    end = time.time()
    last_updated = time.time() - (datetime.datetime.strptime(r['updated_at'], '%Y-%m-%dT%H:%M:%SZ') - datetime.datetime(1970, 1, 1)).total_seconds()
    it_took = end - start
    print 'marketdata.latency {} {} type=quote\nmarketdata.latency {} {} type=request'.format(time.time(), last_updated, time.time(), it_took)

while True:
    t = threading.Timer(2, ticker, ['SPY'])
    t.start()
    time.sleep(2)
