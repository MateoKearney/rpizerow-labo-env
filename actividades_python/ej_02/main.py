#importo las carpetas de led y de espera
from gpiozero import LED
from time import sleep

#declaro los pines de los LEDS
ledrojo = LED(19)
ledazul = LED(26)
ledverde = LED(13)

#genero un bucle que prenda y suspenda los LEDS cada x tiempo
while True:
	ledrojo.on()
	sleep(1)
	ledrojo.off()

	ledverde.on()
	sleep(0.5)
	ledverde.off()

	ledazul.on()
	sleep(4)
	ledazul.off()
