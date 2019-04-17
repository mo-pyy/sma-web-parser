from sma import parser
import paho.mqtt.publish as publish

p = parser('SMA_IP', 'SMA_USER_PASSWORD')
while True:
    publish.single('home/inverter/value', p.value, hostname='example.com')