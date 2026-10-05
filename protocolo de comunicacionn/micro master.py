from machine import Pin
import bluetooth
import time

led = Pin(2, Pin.OUT)
boton = Pin(4, Pin.IN, Pin.PULL_UP)

ble = bluetooth.BLE()
ble.active(True)

print("ESP32 EMISOR")
print("Bluetooth activo")

# Aquí posteriormente hacemos la conexión con el ESP32 receptor

while True:

    if boton.value() == 0:

        # Enciende su propio LED
        led.value(1)

        print("Enviando señal: 1")

        # Aquí enviaremos "1" al ESP32 receptor

        time.sleep(0.5)

    time.sleep(0.1)