class DS3231_I2C:
    ADDRESS = 0x68
    REGISTER = 0x00
    
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.reg = 0x00
    
    def set_time(self, NowTime):
        self.i2c.writeto_mem(int(self.addr),int(self.reg),NowTime)
        
    def read_time(self):
        return self.i2c.readfrom_mem(int(self.addr),int(self.reg),7);