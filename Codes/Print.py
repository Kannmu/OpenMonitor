import multiprocessing
import os
from colorama import Fore,Back,Style,  init
import datetime

init()
multiprocessing.freeze_support()

def DecodeInfo(Info):
    global System_Info,Wifi_Info,Bluetooth_BAT_Info
    System_Info = Info[0]
    Wifi_Info = Info[1]
    Bluetooth_BAT_Info = Info[2]

def LinePrintInto(Info):
    DecodeInfo(Info)
    Now = datetime.datetime.now()
    os.system("cls")

    print(Fore.WHITE + "OpenMonitor", Now.date(),Now.strftime("%A"),Now.strftime("%H:%M"))

    print(
        Fore.RED + "CPU: ",
        str(System_Info["cpu_usage"]),
        "%  ",
        str(round(System_Info["cpu_freq"], 1)),
        "GHz",
        str(System_Info["cpu_model"]),
    )

    # RAM
    print(
        Fore.GREEN + "RAM: ",
        System_Info["ram_usage"],
        "%",
        "(",
        round((System_Info["ram_usage"] / 100) * System_Info["total_ram"], 1),
        "/",
        round(System_Info["total_ram"], 1),
        ")",
    )

    # GPU
    print(
        Fore.BLUE + "GPU: ",
        System_Info["gpu_usage"],
        "%",
        "(",
        round((System_Info["gpu_usage"] / 100) * System_Info["gpu_memory_usage"], 1),
        "/",
        round(System_Info["gpu_memory_usage"], 1),
        ")",
    )
    # Wifi
    print(
        Fore.YELLOW + "WI-FI: ",
        str(Wifi_Info["ssid"]),
        # str(System_info["protocol"]),
        str(round(Wifi_Info["signal_strength"],1)),
        "dBm",
        str(round(Wifi_Info["signal_strength_percent"],2)),
        "%",
    )

    # Bluetooth
    print(
        Fore.CYAN + "Bluetooth Battery: ",
    )
    for i, bluetooth_device in enumerate(Bluetooth_BAT_Info[1]):
        BAT = Bluetooth_BAT_Info[0][i]
        if(BAT <= 20):
            print(Fore.LIGHTRED_EX +"\t",bluetooth_device, ":",BAT,"%")
        else:
            print(Fore.CYAN +"\t",bluetooth_device, ":",BAT,"%")

def TablePrintInfo(Info, table):
    DecodeInfo(Info)
    Now = datetime.datetime.now()
    os.system("cls")
    print(Fore.WHITE + "OpenMonitor", Now.date(),Now.strftime("%A"),Now.strftime("%H:%M"))
    
    table.clear()
    table.add_row(
        [
            "CPU",
            str(System_Info["cpu_usage"]) + "%",
            str(round(System_Info["cpu_freq"], 1)) + "GHz",
        ]
    )
    table.add_row(
        [
            "RAM",
            str(System_Info["ram_usage"]) + "%",
            str(round((System_Info["ram_usage"] / 100) * System_Info["total_ram"], 1))
            + "/"
            + str(round(System_Info["total_ram"], 1)),
        ]
    )
    table.add_row(
        [
            "GPU",
            str(System_Info["gpu_usage"]) + "%",
            str(
                round(
                    (System_Info["gpu_usage"] / 100) * System_Info["gpu_memory_usage"],
                    1,
                )
            )
            + "/"
            + str(round(System_Info["gpu_memory_usage"], 1)),
        ]
    )
    table.add_row(
        ["WI-FI", str(Wifi_Info["ssid"]), str(Wifi_Info["signal_strength"]) + "dBm"]
    )
    for i, bluetooth_device in enumerate(Bluetooth_BAT_Info[1]):
        table.add_row(
            ["Bluetooth Battery", bluetooth_device, str(Bluetooth_BAT_Info[0][i]) + "%"]
        )
        # print("\t",bluetooth_device, ":", Bluetooth_BAT_Info[0][i],"%")
    print(table)
