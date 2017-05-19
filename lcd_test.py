import sys, time, subprocess, re
# using lcd library in the same syspath as this program
import lcd
from subprocess import check_output, STDOUT, CalledProcessError

# simple logfile for headless running
logger = open("lcsd.log", "w")
# declaring all the lists we'll need
ips = []
blocks = []
blocksip = []
# initializing lcd
lcd.lcd_init()
time.sleep(10)

def ifacecheck():		# return 'ip link' process output as 'wlp'
	try:
		wlp = check_output(["ip addr"], shell=True, stderr=STDOUT)
		temp = check_output(["/opt/vc/bin/vcgencmd measure_temp"], shell=True, stderr=STDOUT)
		volt = check_output(["/opt/vc/bin/vcgencmd measure_volts core"], shell=True, stderr=STDOUT)
		voltio = check_output(["/opt/vc/bin/vcgencmd measure_volts "], shell=True, stderr=STDOUT)

		logger.write("\n\nWLP:\n{}".format(wlp))
		logger.write("\n\nTEMP:\n{}".format(temp))
		logger.write("\n\nVOLT:\n{}".format(volt))
		logger.flush()
		return wlp, temp, volt, voltio
	except CalledProcessError as exc :
		retun ("E")

def info(wlp):		# return available interfaces and IPs
	for block in wlp.decode().split(": "):
		if block.startswith('1'):
			pass
		elif block.startswith('lo'):
			pass
		elif block.startswith('<LO'):
			pass
		else :
			blocks.append(block)
	leng = int (len(blocks)/2)
	for i in range(1,leng+1):
		blocksip.append(blocks.pop(i))
	for item in blocksip:
		items = item.split(" ")
		try:
			point = items.index("inet")
		except:
			point = 0
		if point == 0:
			ips.append("Disconnected")
		else : ips.append(items[point+1])
	return blocks,ips

try :
	while True:
		wlp, temp, volt, voltio = ifacecheck()
		temp = temp.decode().strip("\n")
		volt = volt.decode().strip("\n")
		voltio = voltio.decode().strip("\n")
		print (temp)
		print (volt)
		print (voltio)
		ifs,ips = info(wlp)
		count = len(ifs)
		for n in range(count):
			print ("> {}: is {}".format(ifs[n],ips[n]))
		for n in range(count):
			#print ("iface : {} ip :{}".format(ifs[n],ips[n+1]))
			lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
			lcd.lcd_string("{}:".format(ifs[n]), 1)
			time.sleep(.1)
			lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
			lcd.lcd_string("{}".format(ips[n]), 1)
			time.sleep(3)

		lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
		lcd.lcd_string("cpu-{}".format(temp), 1)
		time.sleep(.1)
		lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
		lcd.lcd_string("@ {}".format(volt), 1)
		time.sleep(1.5)
		lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
		lcd.lcd_string("I/O-{}".format(temp), 1)
		time.sleep(.1)
		lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
		lcd.lcd_string("@ {}".format(voltio), 1)
		time.sleep(1.5)
		ips = []
		blocks = []
		blocksip = []
except :
	exit(0)
