from machine import Pin
import bluetooth
import time

led = Pin(2, Pin.OUT)

ble = bluetooth.BLE()
ble.active(True)

print("ESP32 RECEPTOR")
print("Esperando conexión Bluetooth...")

while True:

    # Aquí esperamos recibir la señal

    time.sleep(0.1)