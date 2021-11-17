# Module contains the implementation for the serial communication
# between the pacemaker and the GUI






# Packet Format
#
# [SYNC
#  FN_CODE
#  LRL
#  URL
#  AA
#  VA
#  APW
#  VPW
#  ARP
#  VRP
#  MODE]


import serial
import sys
import glob
import struct
from serial.tools.list_ports import comports
import time

# FRDM_HWID = "0D28:0204" # mbed
FRDM_HWID = "1366:1015"  # JLink
NUCLEO_HWID = "0483:374B"  # ST-Link

def findPorts():
    frdmFound = False
    nucleoFound = False
    nucleoPort = ""
    frdmPort = ""
    while (True):
        for port in comports():
            if FRDM_HWID in port.hwid:
                frdmFound = True
                frdmPort = port.device
            elif NUCLEO_HWID in port.hwid:
                nucleoFound = True
                nucleoPort = port.device
        if (frdmFound and nucleoFound):
            return [nucleoPort, frdmPort]


ports = findPorts()

def transmit():
    packet = []
    packet.append(b'\x16') # SYNC
    #------ THis will not be hard coded in the final. This is only for testing--------
    packet.append(b'\x22') # FN_CODE

    packet.append(b'\x01')
    packet.append(b'\x00')
    packet.append(b'\x00')
    packet += [b'\xf4\x01\x00\x00']
    packet += [b'\xc8\x00']


    #packed_params = struct.pack('i i f f i i i i i', 60, 80, 2.2, 3.2, 1, 2, 200, 400, 1)
    # packet.append((60).to_bytes(8, byteorder="little", signed=False))
    # packet.append((80).to_bytes(8, byteorder="little", signed=False))
    # packet.append(struct.pack("<f", 2.2))
    # packet.append(struct.pack("<f", 3.2))
    # packet.append((1).to_bytes(8, byteorder="little", signed=False))
    # packet.append((2).to_bytes(8, byteorder="little", signed=False))
    # packet.append((200).to_bytes(16, byteorder="little", signed=False))
    # packet.append((400).to_bytes(16, byteorder="little", signed=False))
    # packet.append((1).to_bytes(8, byteorder="little", signed=False))
    packet.append('close')


    print(packet)




    with serial.Serial(ports[1], 115200, timeout=5) as ser:
        for param in packet:
            if param == 'close':
                break

            ser.write(param)
            #print(param)

        print("\n\n\nReceived-----------------------")
        pack = ser.read(size=9)
        print("Pack:", pack)
        test = pack[3:7]
        print("Single: ", test)
        print((struct.unpack("f", test))[0])
        #print(struct.unpack('hhhfi', pack))
        #print("Pack:", int(pack, 16))


transmit()
#receive()
