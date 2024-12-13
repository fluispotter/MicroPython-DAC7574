# MicroPython DAC7574

MicroPython driver for the [DAC7574](https://www.ti.com/product/DAC7574) digital-to-analog converter.

## Usage

The `DAC7574` constructor accepts an I2C instance.

```python
from machine import Pin, I2C
from dac7574 import DAC7574

i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=100000)

dac = DAC7574(i2c)

# Write to channel 1 DAC register.
dac.write_write_dac_register(1, 4095)
```
