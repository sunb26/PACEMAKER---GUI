from serial import Serial   
import struct
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

def transmit_params():


    # Struct.pack everything
    params = b''
    params += struct.pack('B', 1) # SYNC
    params += struct.pack('B', 5) # FN Code - change the number in the argument to test the different modes
    params += struct.pack('H', 30) # LRL
    params += struct.pack('H', 60) # URL
    params += struct.pack('f', 3.5) # AA
    params += struct.pack('f', 3.5) # VA
    params += struct.pack('H', 2) # APW
    params += struct.pack('H', 2) # VPW
    params += struct.pack('H', 200) # ARP
    params += struct.pack('H', 400) # VRP
    params += struct.pack('B', 1) # MODE



    print(len(params))

    with Serial(ports[1], 115200, timeout=3) as pacemaker:
        print(ports[1])
        pacemaker.write(params)

        receive = pacemaker.read(size=21)

        params = struct.unpack("HHffHHHHB", receive)
        print(params)

#def receive_egram():
transmit_params()