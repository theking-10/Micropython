from machine import Pin
import bluetooth
import time

led = Pin(2, Pin.OUT)

ble = bluetooth.BLE()
ble.active(True)

# UUID del servicio
SERVICE_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef0")

# UUID de la característica
CHAR_UUID = bluetooth.UUID("12345678-1234-5678-1234-56789abcdef1")

SERVICE = (
    SERVICE_UUID,
    (
        CHAR_UUID,
        bluetooth.FLAG_READ |
        bluetooth.FLAG_WRITE |
        bluetooth.FLAG_NOTIFY,
    ),
)

((handle,),) = ble.gatts_register_services((SERVICE,))


def recibir(evento, datos):
    if evento == 3:
        mensaje = ble.gatts_read(handle).decode().strip()

        print("Recibido:", mensaje)

        if mensaje == "1":
            led.value(1)
            print("LED ENCENDIDO")

        elif mensaje == "0":
            led.value(0)
            print("LED APAGADO")


ble.irq(recibir)


# Hacer visible el ESP32
nombre = "ESP32_LED"

adv_data = bytearray(
    b"\x02\x01\x06" +
    bytes((len(nombre) + 1, 0x09)) +
    nombre.encode()
)

ble.gap_advertise(100000, adv_data)

print("Bluetooth iniciado")
print("Nombre:", nombre)

while True:
    time.sleep(1)