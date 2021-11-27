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

def transmit_params(user_params):


    # Struct.pack everything
    params = b''
    params += struct.pack('B', 1) # SYNC
    params += struct.pack('B', 3) # FN Code - always going to be set



    params += struct.pack('H', user_params["lrl"]) # LRL
    params += struct.pack('H', user_params["url"]) # URL
    params += struct.pack('f', user_params["aa"]) # AA
    params += struct.pack('f', user_params["va"]) # VA
    params += struct.pack('H', user_params["apw"]) # APW
    params += struct.pack('H', user_params["vpw"]) # VPW
    params += struct.pack('H', user_params["ARP"]) y# ARP
    params += struct.pack('H', user_params["VRP"]) # VRP
    params += struct.pack('H', user_params["msr"]) # msr
    params += struct.pack('H', user_params["favd"]) # favd
    params += struct.pack('H', user_params["asen"]) # asen
    params += struct.pack('H', user_params["vsen"]) # vsen
    params += struct.pack('H', user_params["PVARP"]) # PVARP
    params += struct.pack('H', user_params["hys"]) # hys
    params += struct.pack('H', user_params["rs"]) # rs
    params += struct.pack('H', user_params["at"]) # at
    params += struct.pack('H', user_params["rct"]) # rct
    params += struct.pack('H', user_params["rf"]) # rf
    params += struct.pack('H', user_params["rvt"]) # rvt
    params += struct.pack('B', user_params["mode"]) # MODE



    print(len(params))

    with Serial(ports[1], 115200, timeout=3) as pacemaker:
        print(ports[1])
        pacemaker.write(params)

        receive = pacemaker.read(size=42)

        params = struct.unpack("HHffHHHHB", receive)
        print(params)

def receive_egram():
    params = b''
    params += struct.pack('B', 1) # SYNC
    params += struct.pack('B', 4) # FN Code - always going to be 4 for receive

    params += struct.pack('H', user_params["lrl"]) # LRL
    params += struct.pack('H', user_params["url"]) # URL
    params += struct.pack('f', user_params["aa"]) # AA
    params += struct.pack('f', user_params["va"]) # VA
    params += struct.pack('H', user_params["apw"]) # APW
    params += struct.pack('H', user_params["vpw"]) # VPW
    params += struct.pack('H', user_params["ARP"]) # ARP
    params += struct.pack('H', user_params["VRP"]) # VRP
    params += struct.pack('H', user_params["msr"]) # msr
    params += struct.pack('H', user_params["favd"]) # favd
    params += struct.pack('H', user_params["asen"]) # asen
    params += struct.pack('H', user_params["vsen"]) # vsen
    params += struct.pack('H', user_params["PVARP"]) # PVARP
    params += struct.pack('H', user_params["hys"]) # hys
    params += struct.pack('H', user_params["rs"]) # rs
    params += struct.pack('H', user_params["at"]) # at
    params += struct.pack('H', user_params["rct"]) # rct
    params += struct.pack('H', user_params["rf"]) # rf
    params += struct.pack('H', user_params["rvt"]) # rvt
    params += struct.pack('B', user_params["mode"]) # MODE

    with Serial(ports[1], 115200, timeout=3) as pacemaker:
        print(ports[1])
        pacemaker.write(params)

        receive = pacemaker.read(size=42)

        params = struct.unpack("HHffHHHHB", receive)
        print(params)

transmit_params()