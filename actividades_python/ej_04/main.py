from gpiozero import PWMLED
import ADS1x15, time, math


# Declara el pin de I2C y el registro
ADS = ADS1x15.ADS1115(1,0x48)
ADS.setMode(ADS.MODE_SINGLE)

# Se declaran los pines 19 y 26 para el LED rojo y azul
red = PWMLED(19)
blue = PWMLED(26)
red.value = 0
blue.value = 0

# Hace que la ganancia del ADC sea de +/-6,144V
ADS.setGain(ADS.PGA_4_096V)
# Convierte el valor obtenido por el ADC a un valor de voltaje.
factor = ADS.toVoltage()

# Variables a usar para el cálculo de Temperatura.
vcc = 3.3
vrtermistor = 0
rtermistor = 0
t = 0
## r = Resistencia R1 del divisor de tensión
r1 = 10000
## Factor de aumento del Termistor.
aumento = 3977

while True :
	# Hace que el ADC lea en pin 3 y el pin 1
	Potval = ADS.readADC(3)
	Termval = ADS.readADC(1)
	# Multiplica el valor obtenido por el factor de incremento del ADC
	PotvalV = Potval * factor
	TermvalV = Termval * factor

	# Cálculos para sacar la Temperatura
	rtermistor = (TermvalV*r1)/(3.3 - TermvalV)
	t = (aumento/(math.log10(rtermistor/r1)+(aumento/298.0)) - 273.15)

	# Funciones para que cambie de color el LED, comparando si el V del pot es mayor que el del term (color rojo, máx 5°)
	if (PotvalV>TermvalV):
		red.value = (PotvalV-TermvalV)*0.2
		blue.value = 0
		if (red.value>1):
			red.value = 1
		time.sleep(1)

	# Funciones para que cambie de color el LED, comparando si el V del term es mayor que el del pot (color azul, máx 5°)
	if (PotvalV<TermvalV):
		blue.value = (TermvalV-PotvalV)*0.2
		red.value = 0
		if (blue.value>1):
			blue.value = 1
		time.sleep(1)

	# Muestra valores de voltaje de Termistor y Potenciometro, y la temperatura
	print("Valor del Termistor {0:.3f} V".format(TermvalV))
	print("Valor del Potenciómetro {0:.3f} V".format(PotvalV))
	print("Valor  del Termistor {0:.3f} T".format(t))

	time.sleep(2)
