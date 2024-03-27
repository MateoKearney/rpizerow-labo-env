from gpiozero import LED, Button
from signal import pause

#se importa el led y el boton para que el programa los identifique
#se importa la función de pausar

led = LED(13) #se selecciona el gpio13 como salida para el LED
button = Button(18) #se selecciona el gpio18 como salida para el botón

button.when_pressed = led.on #el botón se presiona, funciona el LED
button.when_released = led.off #el botón se suelta, se apaga el LED

pause()
