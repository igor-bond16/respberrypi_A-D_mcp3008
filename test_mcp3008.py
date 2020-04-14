import spidev
#from time import sleep

spi = spidev.SpiDev()
spi.open(0,0)
#active = True

def readADC(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    print(adc)
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def convertVolts(data,vref):
    volts = (data*vref)/float(1023)
    volts = round(volts,4)
    return volts

if __name__ == '__main__':
#while active == True:
#    try:
    ch = 0
    data = readADC(ch)
    print("adc: {:8}".format(data))
    v = 5.0
    volts = convertVolts(data,v)
    print("volts: {:8.2f}".format(volts))
#    except KeyboardInterrupt:
        #active = False
        
