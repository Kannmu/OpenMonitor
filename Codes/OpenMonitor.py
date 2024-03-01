import os
import psutil
import cpuinfo
import GPUtil
import time
import pywifi
import numpy
from prettytable import PrettyTable
import argparse

from colorama import Fore, init

init()

def get_system_info():
    """
    Get the current CPU usage, CPU temperature, CPU model, RAM usage, total RAM,
    GPU usage, GPU memory usage, total GPU memory, system power consumption,
    and WiFi network information.

    Returns:
        A dictionary containing the following system information:
        - 'cpu_usage': Current CPU usage as a percentage.
        - 'cpu_model': CPU model name.
        - 'ram_usage': Current RAM usage as a percentage.
        - 'total_ram': Total RAM of the system in gigabytes.
        - 'gpu_usage': Current GPU usage as a percentage.
        - 'gpu_memory_usage': Current GPU memory usage as a percentage.
        - 'total_gpu_memory': Total GPU memory in bytes.
        - 'ssid': SSID of the currently connected WiFi network.
        - 'signal_strength': Signal strength of the currently connected WiFi network.
        - 'signal_strength_Percent': Signal strength of the currently connected WiFi network as a percentage.
        - 'protocol': Authentication protocol of the currently connected WiFi network.
    """
    # Get CPU usage as a percentage
    cpu_usage = psutil.cpu_percent()
    cpu_freq = psutil.cpu_freq().current / 1000

    # Get CPU model name
    cpu_model = cpuinfo.get_cpu_info()["brand_raw"]

    # Get RAM usage as a percentage
    ram_usage = psutil.virtual_memory().percent

    # Get total RAM of the system in gigabytes
    total_ram = psutil.virtual_memory().total / (1024**3)

    # Get GPU usage as a percentage
    gpus = GPUtil.getGPUs()
    gpu_usage = gpus[0].load * 100

    # Get GPU memory usage as a percentage
    gpu_memory_usage = gpus[0].memoryUtil * 100

    # Get total GPU memory in bytes
    total_gpu_memory = gpus[0].memoryTotal

    # Extract the required information from the WiFi information
    wifi = pywifi.PyWiFi()

    ifaces = wifi.interfaces()[0]
    if ifaces.status() == pywifi.const.IFACE_CONNECTED:
        # Get the current connected WiFi network
        current_network = ifaces.scan_results()[0]

        # Extract the required information from the WiFi network
        ssid = current_network.ssid
        signal_strength = current_network.signal
        signal_strength_Percent = 2 * (signal_strength + 100)
        protocol = current_network.auth

    # Create a dictionary to store the system information
    system_info = {
        "cpu_usage": cpu_usage,
        "cpu_freq": cpu_freq,
        "cpu_model": cpu_model,
        "ram_usage": ram_usage,
        "total_ram": total_ram,
        "gpu_usage": gpu_usage,
        "gpu_memory_usage": gpu_memory_usage,
        "total_gpu_memory": total_gpu_memory,
        "ssid": ssid,
        "signal_strength": signal_strength,
        "signal_strength_Percent": signal_strength_Percent,
        "protocol": protocol,
    }

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
    table = PrettyTable()
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
    parser = argparse.ArgumentParser(description="OpenMonitor")
    parser.add_argument("-t", "--TablePrintInfo", action="store_true", help="Show info in table")
    args = parser.parse_args()
    while True:
        if args.TablePrintInfo:
            TablePrintInfo()
        else:
            LinePrintInto()
        time.sleep(1)
