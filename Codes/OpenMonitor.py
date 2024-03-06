import multiprocessing
import os
import time
from prettytable import PrettyTable
import argparse
import InfoObtain as io
import Print as p
from colorama import Fore

table = PrettyTable()

Bluetooth_BAT_Obtain_Gap = 30  # Time gap in second of func, default to 30
Wifi_Obtain_Gap = 10  # Time gap in second of func, default to 10

if __name__ == "__main__":
    os.system("cls")

    TimeCount = 0
    # Disable multiprocessing
    multiprocessing.freeze_support()

    # Parameter Decompose
    parser = argparse.ArgumentParser(description="OpenMonitor")

    parser.add_argument(
        "-t", "--TablePrintInfo", action="store_true", help="Show info in table"
    )

    args = parser.parse_args()

    print(
        Fore.RED + "Now Loading..."
    )
    # Start Loop
    while True:
        # Get System Data
        System_Info = io.get_system_stats()

        if TimeCount%Wifi_Obtain_Gap == 0:
            Wifi_info = io.get_wifi_info()
        
        if TimeCount%Bluetooth_BAT_Obtain_Gap == 0:
            Bluetooth_BAT_Info = io.get_bluetooth_bat()

        Info = [
            System_Info, 
            Wifi_info, 
            Bluetooth_BAT_Info
        ]

        os.system("cls")
        if args.TablePrintInfo:
            p.TablePrintInfo(Info, table)
        else:
            p.LinePrintInto(Info)

        # Break
        time.sleep(1)
        TimeCount += 1
