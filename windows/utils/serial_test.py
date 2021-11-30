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
    params += struct.pack('d', 30) # LRL
    params += struct.pack('H', 60) # URL don't use
    params += struct.pack('f', 5) # AA
    params += struct.pack('f', 5) # VA
    params += struct.pack('d', 1) # APW
    params += struct.pack('d', 1) # VPW
    params += struct.pack('d', 200) # ARP
    params += struct.pack('d', 400) # VRP
    params += struct.pack('d', 120) # MSR
    params += struct.pack('d', 5) # FAVD
    params += struct.pack('f', 2) # ASEN don't use
    params += struct.pack('f', 3) # VSEN don't use
    params += struct.pack('H', 150) # PVARP don't use
    params += struct.pack('B', 0) # HYS don't use
    params += struct.pack('B', 3) # RS don't use
    params += struct.pack('d', 1) # AT
    params += struct.pack('d', 3000) # RCT
    params += struct.pack('d', 8) # RF
    params += struct.pack('d', 4000) # RVT
    params += struct.pack('B', 1)  # MODE


    print(len(params))

    with Serial(ports[1], 115200, timeout=5) as pacemaker:
        print(ports[1])
        pacemaker.write(params)

        if params[1] == 3: #ECHO
            receive = pacemaker.read(size=111)

            params = struct.unpack("=dHffddddddffHBBddddB", receive)
            print(params)

        elif params[1] == 4: #E_GRAM
            while params[1] != 5:
                receive = pacemaker.read(size=127)
                params = struct.unpack("=dHffddddddffHBBddddBdd", receive)
                print("(", params[20], ",", params[21], ")\n")
                #params[20] is atr signal and params[21] is vent signal

#def receive_egram():
transmit_params()