from sma import parser
from bottle import get, run

p = parser('SMA_IP', 'SMA_USER_PASSWORD')

@get('/value')
def sendvalue():
    return p.value

run(host='127.0.0.1', port=1080)