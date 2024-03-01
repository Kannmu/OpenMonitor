import os
import psutil
import cpuinfo
import GPUtil
import time
import pywifi

from colorama import Fore, init

init()


def get_system_info():
    """
    Get the current CPU usage, CPU temperature, CPU model, RAM usage, total RAM,
    GPU usage, GPU memory usage, and total GPU memory of the system.

    Returns:
        A dictionary containing the following system information:
        - 'cpu_usage': Current CPU usage as a percentage.
        - 'cpu_temp': Current CPU temperature in Celsius.
        - 'cpu_model': CPU model name.
        - 'ram_usage': Current RAM usage as a percentage.
        - 'total_ram': Total RAM of the system in bytes.
        - 'gpu_usage': Current GPU usage as a percentage.
        - 'gpu_memory_usage': Current GPU memory usage as a percentage.
        - 'total_gpu_memory': Total GPU memory in bytes.
    """
    # Get CPU usage as a percentage
    cpu_usage = psutil.cpu_percent()

    # Get CPU temperature in Celsius
    # cpu_temp = psutil.sensors_temperatures()['cpu_thermal'][0].current

    # Get CPU model name
    cpu_model = cpuinfo.get_cpu_info()["brand_raw"]

    # Get RAM usage as a percentage
    ram_usage = psutil.virtual_memory().percent

    # Get total RAM of the system in bytes
    total_ram = psutil.virtual_memory().total

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
        signal_strength_dBm = (signal_strength / 2) - 100
        protocol = current_network.auth

    # Create a dictionary to store the system information
    system_info = {
        "cpu_usage": cpu_usage,
        # 'cpu_temp': cpu_temp,
        "cpu_model": cpu_model,
        "ram_usage": ram_usage,
        "total_ram": total_ram / (1024**3),
        "gpu_usage": gpu_usage,
        "gpu_memory_usage": gpu_memory_usage,
        "total_gpu_memory": total_gpu_memory,
        "ssid": ssid,
        'signal_strength': signal_strength,
        'signal_strength_dBm':signal_strength_dBm,
        'protocol': protocol,
    }

    # Return the system information
    return system_info


if __name__ == "__main__":
    while True:
        System_info = get_system_info()
        os.system("cls")

        # CPU
        print(
            Fore.RED + "CPU: ",
            str(System_info["cpu_usage"]),
            "%  ",
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
            round(
                (System_info["gpu_usage"] / 100) * System_info["gpu_memory_usage"], 1
            ),
            "/",
            round(System_info["gpu_memory_usage"], 1),
            ")",
        )

        # Wifi
        print(
            Fore.RED + "WI-FI: ",
            str(System_info["ssid"]),
            str(System_info["protocol"]),
            str(System_info["signal_strength"]),
            str(System_info["signal_strength_dBm"]),
        )

        # os.system("netsh WLAN show interfaces")

        time.sleep(1)
