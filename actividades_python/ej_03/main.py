from gpiozero import LED, Buzzer
from time import sleep

LEDazul = LED(26)
LEDverde = LED(13)
LEDrojo = LED(19)
buzzer = Buzzer(15)

while True:
	cmd = input("Tirame el comando ")

	print("Indique promt: ", cmd)

	if(cmd == "buzz on"):
		buzzer.on()

	elif(cmd  == "buzz off"):
		buzzer.off()

	if(cmd == "rgb red"):
		LEDazul.off()
		LEDverde.off()
		LEDrojo.on()

	if(cmd == "rgb blue"):
		LEDrojo.off()
		LEDverde.off()
		LEDazul.on()

	if(cmd == "rgb green"):
		LEDazul.off()
		LEDrojo.off()
		LEDverde.on()
