from machine import UART

serial = UART(0)

serial.init(9600, bits=8, parity=None, stop=1)

count = 0
while True:
    if serial.any() > 0:
        print(serial.read().decode('utf-8'))
    serial.write(bytes(count, 'utf-8'))
    count += 1

