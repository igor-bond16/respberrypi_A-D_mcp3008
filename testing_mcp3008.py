from gpiozero import MCP3008
##from test_mcp3008 import convertVolts

vref = 5.0

pot = MCP3008(channel=0)
#volts = convertVolts(pot.value,vref)
#print("volts: {:8.2f}".format(volts))
