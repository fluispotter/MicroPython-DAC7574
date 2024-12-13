UPDATE_MODE_WRITE_TEMPORARY_REGISTER = 0
UPDATE_MODE_WRITE_DAC_REGISTER = 1
UPDATE_MODE_SYNCHRONIZE = 2
UPDATE_MODE_BROADCAST = 3

POWER_NORNAL = 0
POWER_DOWN = 1

POWER_DOWN_MODE_NORMAL = 0b000000000000
POWER_DOWN_MODE_1_KOHM_GND = 0b010000000000
POWER_DOWN_MODE_100_KOHM_GND = 0b100000000000
POWER_DOWN_MODE_HIGH_IMPEDENCE = 0b110000000000

BROADCAST_UPDATE_TEMPORARY = 0
BROADCAST_UPDATE_DATA = 1

class DAC7574:
    _BUFFER_24 = bytearray(3)

    def __init__(self, i2c, address=0x4c):
        self._i2c = i2c
        self._address = address

    def write_control(self, update_mode, channel, power_down, data):
        self._BUFFER_24[0] = (update_mode << 4) | (channel << 1) | power_down
        self._BUFFER_24[1] = (data >> 4) & 0xff
        self._BUFFER_24[2] = (data << 4) & 0xff
        self._i2c.writeto(self._address, self._BUFFER_24)

    def write_temporary_register(self, channel, value):
        self.write_control(UPDATE_MODE_WRITE_TEMPORARY_REGISTER, channel, POWER_NORNAL, value)

    def write_dac_register(self, channel, value):
        self.write_control(UPDATE_MODE_WRITE_DAC_REGISTER, channel, POWER_NORNAL, value)

    def write_dac_register_and_synchronize(self, channel, value):
        self.write_control(UPDATE_MODE_SYNCHRONIZE, channel, POWER_NORNAL, value)
