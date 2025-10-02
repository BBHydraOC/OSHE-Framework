# How to blink a LED connected to GP2
import EasyMCP2221
from time import sleep

# Connect to the device
mcp = EasyMCP2221.Device()

# Set GP2 for General Purpose Input Output, as an Output.
mcp.set_pin_function(gp2 = "GPIO_OUT")

#Scan for I2C Devices on the bus
devices = 0
for addr in range(0, 0x80):
    try:
        mcp.I2C_read(addr)
        data = mcp.I2C_read(
            addr = addr,
            size = 1)
        #Check if the byte is invalid
        if(data != b'\x07'):
            devices = devices + 1

    except EasyMCP2221.exceptions.NotAckError:
        pass
    
# Create blank array with length equal to the number of devices on I2C Bus
addrs = [0] * devices
devices = 0
    
for addr in range(0, 0x80):
    try:
        mcp.I2C_read(addr)
        data = mcp.I2C_read(
            addr = addr,
            size = 1)
        
        #Check if the byte is invalid
        if(data != b'\x07'):
            addrs[devices] = addr
            devices = devices + 1
        

    except EasyMCP2221.exceptions.NotAckError:
        pass

#Query all devices for debug information
while True:
    
    mcp.GPIO_write(gp2 = False)
    sleep(0.25)
    
    for i in range(0, devices):
        slaveaddr = addrs[i]
        data = mcp.I2C_read(
            addr = slaveaddr,
            size = 2)
        
        print("Recieved: " + data.decode('utf-8'))
        print("Recieved from: 0x%02X" % (slaveaddr) )
            
    mcp.GPIO_write(gp2 = True)
    sleep(0.25)
    
    
    
