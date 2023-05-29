from machine import UART

serial = UART(0, 9600)

serial.init()

count = 0
while True:
    if serial.any() > 0:
        message = serial.read()
        print(message)
    serial.write(bytes(str(count), 'utf-8'))
    count += 1
