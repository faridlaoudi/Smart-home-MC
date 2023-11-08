import serial

ser=serial.Serial('/dev/serial0',baudrate=9600,timeout=1)

try:
    while True:
        data=ser.read(10)
        print(data)
except KeyboardInterrupt:
    ser.close() 