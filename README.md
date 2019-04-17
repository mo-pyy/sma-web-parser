# sma-web-parser
## Intention
This is a parser which parses the power value of your sma inverter web interface. You may ask, why parse the value from the web interface when there is a modbus interface. Sadly my sma inverter came with modbus disabled. To enable it, you would need the installers password, which I was not given. So no modbus for me :( Also some old sma inverters came without modbus support at all.

## Installation

```
git clone https://github.com/mo-pyy/sma-web-parser.git
cd sma-web-parser
python setup.py install
```

## Usage

Create a client using:
```python
from sma import parser

p = parser('SMA_IP', 'SMA_USER_PASSWORD')
```
You can get the current power value like this:
```python
current_val = p.value
```

Because the actual value is changing very fast, a moving average is being calculated.
By default the actual value is being requested every 20 seconds and the moving average is 300 seconds long.
This means that the actual value is being averaged with the last 14 values.
You can change this values by parsing them to the constructor:
```python
from sma import parser

p = parser('SMA_IP', 'SMA_USER_PASSWORD', requests_delay = 20, moving_average_size = 300)
```

You can also enable logging. By default a log file called 'log.csv' is created in the current directory.
```python
from sma import parser

p = parser('SMA_IP', 'SMA_USER_PASSWORD', log=True, data_dir = '')
```
