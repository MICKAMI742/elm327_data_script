import asyncio
from bleak import BleakScanner
import socket

# This function will scan for nearby devices and connect to the first one it finds
async def connect():
    nearby = await BleakScanner.discover()
    return nearby
    
nearby_devices = asyncio.run(connect())

def choose_device(nearby_devices):
    for i, device in enumerate(nearby_devices):
        print(f"{i}: {device.name}, {device.address}")
    choice = int(input("Choose a device to connect to: "))
    return nearby_devices[choice]

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

# initiate a connection to the first device found
soc = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

device = choose_device(nearby_devices)

connect_to_device(device)