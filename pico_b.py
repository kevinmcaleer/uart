from machine import UART

serial = UART(0, 9600, bits=8, parity=None, stop=1)

serial.init()

count = 0
while True:
    if serial.any() > 0:
        message = serial.read()
        decoded_message = bytes(c for c in message if c < 128).decode("utf-8")
        print(decoded_message)
    serial.write(bytes(str(count), "utf-8"))
    count += 1
