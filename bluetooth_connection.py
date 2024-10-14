import asyncio
from bleak import BleakScanner
import socket

# This function will scan for nearby devices and connect to the first one it finds
async def search():
    nearby = await BleakScanner.discover()
    return nearby
    
nearby_devices = asyncio.run(search())

# This function provides you to choose the device you want to connect to
def choose_device(nearby_devices):
    for i, device in enumerate(nearby_devices):
        print(f"{i}: {device.name}, {device.address}")
    choice = int(input("Choose a device to connect to: "))
    return nearby_devices[choice]

# This function connects to the specific device
def connect_to_device(device):
    address = device.address
    port = 4
    try:
        if(soc.connect((address, port))):
            print("Connected to device")
            return 1
    except:
        print("Connection failed")
        return 0

# This function closes socket and ending connection with device, it will be called at the end of obd_communication.py
def disconnect():
    soc.close()
    print("Disconnected from device")

# initiate a connection to the first device found
soc = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

device = choose_device(nearby_devices)

connect_to_device(device)