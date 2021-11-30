from serial import Serial
import struct
import serial
import sys
import glob
import struct
from serial.tools.list_ports import comports
import time

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

        else:
            return False


class serial_packet:

    def __init__(self, user_params):
        self.user_params = user_params

        self.param_list = ["lrl", "url", "aa", "va", "apw", "vpw", "ARP", "VRP", "msr", "favd", "asen", "vsen", "PVARP", 
                            "hys", "rs", "at", "rct", "rf", "rvt", "mode"]


    def transmit_params(self, fn_code):
        ports = findPorts()

        for parameter in self.param_list:
            if parameter not in self.user_params.keys():
                self.user_params[parameter] = 1

        # Struct.pack everything
        params = b''
        params += struct.pack('B', 1)  # SYNC
        params += struct.pack('B', fn_code)  # FN Code - always going to be set

        print(self.user_params)

        params += struct.pack('d', float(self.user_params["lrl"]))  # LRL
        params += struct.pack('H', int(self.user_params["url"]))  # URL
        params += struct.pack('f', float(self.user_params["aa"]))  # AA
        params += struct.pack('f', float(self.user_params["va"]))  # VA
        params += struct.pack('d', float(self.user_params["apw"]))  # APW
        params += struct.pack('d', float(self.user_params["vpw"]))  # VPW
        params += struct.pack('d', float(self.user_params["ARP"]))  # ARP
        params += struct.pack('d', float(self.user_params["VRP"]))  # VRP
        params += struct.pack('d', float(self.user_params["msr"]))  # msr
        params += struct.pack('d', float(self.user_params["favd"]))  # favd
        params += struct.pack('f', float(self.user_params["asen"]))  # asen
        params += struct.pack('f', float(self.user_params["vsen"]))  # vsen
        params += struct.pack('H', int(self.user_params["PVARP"]))  # PVARP
        params += struct.pack('B', int(self.user_params["hys"]))  # hys
        params += struct.pack('B', int(self.user_params["rs"]))  # rs
        params += struct.pack('d', float(self.user_params["at"]))  # at
        params += struct.pack('d', float(self.user_params["rct"]))  # rct
        params += struct.pack('d', float(self.user_params["rf"]))  # rf
        params += struct.pack('d', float(self.user_params["rvt"]))  # rvt
        params += struct.pack('B', self.user_params["mode"])  # MODE

        print(len(params))
        print(struct.unpack("=BBdHffddddddffHBBddddB", params))

        with Serial(ports[1], 115200, timeout=3) as pacemaker:
            pacemaker.flush()

            print(ports[1])
            pacemaker.write(params)

            if params[1] == 3:
                receive = pacemaker.read(size=111)

                params = struct.unpack("=dHffddddddffHBBddddB", receive)
                print(params)
                return params

            elif params[1] == 4:
                while True:
                    receive = pacemaker.read(size=127)
                    #print(len(receive), "---------------------------------------------------------------------")
                    params = struct.unpack("=dHffddddddffHBBddddBdd", receive)
                    #print("(", params[20], ",", params[21], ")\n")
                    atrium_amp = params[20]
                    ven_amp = params[21]
                    return [atrium_amp, ven_amp]

    # def receive_egram(self):
    #     params = b''
    #     params += struct.pack('B', 1)  # SYNC
    #     params += struct.pack('B', 4)  # FN Code - always going to be 4 for receive

    #     params += struct.pack('H', user_params["lrl"])  # LRL
    #     params += struct.pack('H', user_params["url"])  # URL
    #     params += struct.pack('f', user_params["aa"])  # AA
    #     params += struct.pack('f', user_params["va"])  # VA
    #     params += struct.pack('H', user_params["apw"])  # APW
    #     params += struct.pack('H', user_params["vpw"])  # VPW
    #     params += struct.pack('H', user_params["ARP"])  # ARP
    #     params += struct.pack('H', user_params["VRP"])  # VRP
    #     params += struct.pack('H', user_params["msr"])  # msr
    #     params += struct.pack('H', user_params["favd"])  # favd
    #     params += struct.pack('H', user_params["asen"])  # asen
    #     params += struct.pack('H', user_params["vsen"])  # vsen
    #     params += struct.pack('H', user_params["PVARP"])  # PVARP
    #     params += struct.pack('H', user_params["hys"])  # hys
    #     params += struct.pack('H', user_params["rs"])  # rs
    #     params += struct.pack('H', user_params["at"])  # at
    #     params += struct.pack('H', user_params["rct"])  # rct
    #     params += struct.pack('H', user_params["rf"])  # rf
    #     params += struct.pack('H', user_params["rvt"])  # rvt
    #     params += struct.pack('B', user_params["mode"])  # MODE

    #     with Serial(ports[1], 115200, timeout=3) as pacemaker:
    #         print(ports[1])
    #         pacemaker.write(params)

    #         receive = pacemaker.read(size=42)

    #         params = struct.unpack("=HHffHHHHB", receive)
    #         print(params)
