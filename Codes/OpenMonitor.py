import multiprocessing
import os
import psutil
import cpuinfo
import GPUtil
import time
import pywifi
from prettytable import PrettyTable
import argparse

from colorama import Fore, init

init()
table = PrettyTable()

def get_system_info():
    """
    Get the current CPU usage, CPU temperature, CPU model, RAM usage, total RAM,
    GPU usage, GPU memory usage, total GPU memory, system power consumption,
    and WiFi network information.

    Returns:
        A dictionary containing the system information.
    """
    system_info = {}

    try:
        # Get CPU usage as a percentage
        system_info["cpu_usage"] = psutil.cpu_percent()
        system_info["cpu_freq"] = psutil.cpu_freq().current / 1000

        # Get CPU model name
        system_info["cpu_model"] = cpuinfo.get_cpu_info()["brand_raw"]

        # Get RAM usage as a percentage
        system_info["ram_usage"] = psutil.virtual_memory().percent

        # Get total RAM of the system in gigabytes
        system_info["total_ram"] = psutil.virtual_memory().total / (1024**3)

        # Get GPU usage as a percentage
        gpus = GPUtil.getGPUs()
        system_info["gpu_usage"] = gpus[0].load * 100

        # Get GPU memory usage as a percentage
        system_info["gpu_memory_usage"] = gpus[0].memoryUtil * 100

        # Get total GPU memory in bytes
        system_info["total_gpu_memory"] = gpus[0].memoryTotal

    except Exception as e:
        # Handle exceptions and assign default values
        system_info["cpu_usage"] = 0
        system_info["cpu_freq"] = 0
        system_info["cpu_model"] = "N/A"
        system_info["ram_usage"] = 0
        system_info["total_ram"] = 0
        system_info["gpu_usage"] = 0
        system_info["gpu_memory_usage"] = 0
        system_info["total_gpu_memory"] = 0

    try:
        # Extract the required information from the WiFi information
        wifi = pywifi.PyWiFi()

        ifaces = wifi.interfaces()[0]
        if ifaces.status() == pywifi.const.IFACE_CONNECTED:
            # Get the current connected WiFi network
            current_network = ifaces.scan_results()[0]

            # Extract the required information from the WiFi network
            system_info["ssid"] = current_network.ssid
            system_info["signal_strength"] = current_network.signal
            system_info["signal_strength_Percent"] = 2 * (current_network.signal + 100)
            system_info["protocol"] = current_network.auth
        else:
            system_info["ssid"] = "N/A"
            system_info["signal_strength"] = 0
            system_info["signal_strength_Percent"] = 0
            system_info["protocol"] = "N/A"

    except Exception as e:
        # Handle exceptions and assign default values
        system_info["ssid"] = "N/A"
        system_info["signal_strength"] = 0
        system_info["signal_strength_Percent"] = 0
        system_info["protocol"] = "N/A"

    # Return the system information
    return system_info


def LinePrintInto():
    System_info = get_system_info()
    os.system("cls")
    print(
        Fore.RED + "CPU: ",
        str(System_info["cpu_usage"]),
        "%  ",
        str(round(System_info["cpu_freq"], 1)),
        "GHz",
        str(System_info["cpu_model"]),
    )

    # RAM
    print(
        Fore.GREEN + "RAM: ",
        System_info["ram_usage"],
        "%",
        "(",
        round((System_info["ram_usage"] / 100) * System_info["total_ram"], 1),
        "/",
        round(System_info["total_ram"], 1),
        ")",
    )

    # GPU
    print(
        Fore.BLUE + "GPU: ",
        System_info["gpu_usage"],
        "%",
        "(",
        round((System_info["gpu_usage"] / 100) * System_info["gpu_memory_usage"], 1),
        "/",
        round(System_info["gpu_memory_usage"], 1),
        ")",
    )
    # Wifi
    print(
        Fore.YELLOW + "WI-FI: ",
        str(System_info["ssid"]),
        # str(System_info["protocol"]),
        System_info["signal_strength"],
        "dBm",
        str(System_info["signal_strength_Percent"]),
        "%",
    )


def TablePrintInfo():
    System_info = get_system_info()
    os.system("cls")
    table.clear()
    table.add_row(
        [
            "CPU",
            str(System_info["cpu_usage"]) + "%",
            str(round(System_info["cpu_freq"], 1)) + "GHz",
        ]
    )
    table.add_row(
        [
            "RAM",
            str(System_info["ram_usage"]) + "%",
            str(round((System_info["ram_usage"] / 100) * System_info["total_ram"], 1))
            + "/"
            + str(round(System_info["total_ram"], 1)),
        ]
    )
    table.add_row(
        [
            "GPU",
            str(System_info["gpu_usage"]) + "%",
            str(
                round(
                    (System_info["gpu_usage"] / 100) * System_info["gpu_memory_usage"],
                    1,
                )
            )
            + "/"
            + str(round(System_info["gpu_memory_usage"], 1)),
        ]
    )
    table.add_row(
        [
            "WI-FI", 
            str(System_info["ssid"]), 
            str(System_info["signal_strength"]) + "dBm"
        ]
    )
    print(table)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    parser = argparse.ArgumentParser(description="OpenMonitor")
    parser.add_argument("-t", "--TablePrintInfo", action="store_true", help="Show info in table")
    args = parser.parse_args()
    while True:
        if args.TablePrintInfo:
            TablePrintInfo()
        else:
            LinePrintInto()
        time.sleep(1)
