import sys, time

sys.path.append('/home/alarm/gpio')

import lcd

lcd.lcd_init()

true = True

while true == True:

	inin = input(">")

	lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
	lcd.lcd_string(inin, 2)
	time.sleep(1)
#	lcd.GPIO.cleanup()
