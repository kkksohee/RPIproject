# smbus library
import smbus

# time library
from time import* 
import I2C_driver as LCD

bus = smbus.SMBus(1)

# IC address
address = 0x53

# x-axis, y-axis, z-axis adress
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

# ADXL345 init
def init_ADXL345():    
    bus.write_byte_data(address, 0x2D, 0x08)

# data measure
def measure_acc(adr):    
    acc0 = bus.read_byte_data(address, adr)

    acc1 = bus.read_byte_data(address, adr + 1)

    acc = (acc1 << 8) + acc0

    if acc > 0x1FF:
        acc = (65536 - acc) * -1

    acc = acc * 3.9 / 1000

    return acc




def main():
    print(bus)
    init_ADXL345()
    mylcd=LCD.lcd()

    a=input()
    if a=='1':
        mylcd.lcd_display_string("PRi I2C test",1)
        sleep(2)
        mylcd.lcd_clear()

    elif a=='2':
        x_acc = measure_acc(x_adr)
        y_acc = measure_acc(y_adr)
        z_acc = measure_acc(z_adr)

        print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')

        sleep(1)
        
    else:
        print('error')
    
        
if __name__ == '__main__':
    main()



