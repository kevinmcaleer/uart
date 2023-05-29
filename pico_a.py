from machine import UART

serial = UART(0)

serial.init(9600, bits=8, parity=None, stop=1)

count = 0
while True:
    if serial.any() > 0:
        message = serial.read()
        print(message)
    serial.write(bytes(str(count), 'utf-8'))
    count += 1

