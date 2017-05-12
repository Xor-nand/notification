import sys, time, subprocess
sys.path.append('/home/alarm/gpio')
import lcd
from subprocess import check_output, STDOUT, CalledProcessError

lcd.lcd_init()

def myip():
	try:
		answer = check_output(["awk '{printf \"%3.1f°C\\n", $1/1000}' /sys/class/thermal/thermal_zone0/temp"], shell=True, stderr=STDOUT)
		return answer
	except CalledProcessError as exc :
		return 1

def sdvolt(sdram):
	pass

def cpu():
	pass

def loopmode():
	cpu = cputemp()
	sdram = sdvolt("sdram_c")
	sdrami = sdvolt("sdram_i")
	sdramp = sdvolt("sdram_p")
	myip = ip()

	print ip

#ifconfig | sed -En 's/127.0.0.1//;s/.*inet (addr:)?(([0-9]*\.){3}[0-9]*).*/\2/p'

#while true == True:

	#inin = input(">")

	#lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
	#lcd.lcd_string(inin, 2)
	#time.sleep(1)
#	lcd.GPIO.cleanup()
