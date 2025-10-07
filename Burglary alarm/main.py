import machine
import time

pir = machine.Pin(28, machine.Pin.IN)

while True:
    if pir.value():              
        print("Motion detected!")  
    time.sleep(1)