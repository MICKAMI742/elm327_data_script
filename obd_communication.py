import bluetooth_connection
import serial

serPort = serial.Serial(
        port = "",
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1,
    )
# this function will send a signal by k-line to the car
def send_signal():
    init_byte = 0x33

    if serPort.is_open():
        print("Port is open")
        serPort.write(init_byte)
        response = serPort.readline()

    return response

def main():
   bluetooth_connection.main()
   send_signal()

if __name__ == "__main__":
    main()
    serPort.close()
    bluetooth_connection.disconnect()