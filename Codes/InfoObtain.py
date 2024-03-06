import math
import os
import psutil
import cpuinfo
import GPUtil
import pywifi
import subprocess
import json
import Utilities as u

def get_bluetooth_bat():
    # PowerShell command to retrieve Bluetooth device information
    powershell_command = r"""
    $devices = Get-PnpDevice | Where-Object {($_.Class -EQ 'Bluetooth' -and $_.InstanceId -Like 'BTHLE\*') -or ($_.Class -EQ 'System' -and $_.InstanceId -Like 'BTHENUM\*')}
    $res = $devices | Get-PnpDeviceProperty -KeyName '{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2' | Where-Object Type -ne Empty
    $hash = @{FriendlyName = @(); InstanceId = @(); Battery = @()}
    $res | ForEach-Object {
        $hash["FriendlyName"] += ($devices | Where-Object InstanceId -EQ $_.InstanceId).FriendlyName;
        $hash["InstanceId"] += $_.InstanceId;
        $hash["Battery"] += $_.Data;
    }
    $hash | ConvertTo-Json
    """

    # Execute the PowerShell command and capture the output
    result = subprocess.run(
        ["powershell", "-Command", powershell_command], capture_output=True, text=True
    )
    os.system("cls")  # Clear the console screen

    output = result.stdout.strip()

    # Parse the output as JSON
    output = json.loads(output)

    # Delete the "InstanceId" key from the output dictionary
    del output["InstanceId"]

    n = len(list(output.values())[0])

    result = [[0] * n for _ in range(2)]

    for i, values in enumerate(output.values()):
        result[i] = values

    result = u.sort_matrix_by_row(result, 0)

    return result

def get_wifi_info():
    """
    Get the WiFi network information.

    Returns:
        A dictionary containing the WiFi network information.
    """
    wifi_info = {}

    try:
        wifi = pywifi.PyWiFi()
        ifaces = wifi.interfaces()[0]

        if ifaces.status() == pywifi.const.IFACE_CONNECTED:
            current_network = ifaces.scan_results()[0]
            wifi_info["ssid"] = current_network.ssid
            wifi_info["signal_strength"] = current_network.signal
            wifi_info["signal_strength_percent"] = (1 - (1 / math.pow(10, -current_network.signal/10))) * 100
            wifi_info["protocol"] = current_network.auth
        else:
            wifi_info["ssid"] = "N/A"
            wifi_info["signal_strength"] = 0
            wifi_info["signal_strength_percent"] = 0
            wifi_info["protocol"] = "N/A"

    except Exception as e:
        wifi_info["ssid"] = "N/A"
        wifi_info["signal_strength"] = 0
        wifi_info["signal_strength_percent"] = 0
        wifi_info["protocol"] = "N/A"

    return wifi_info

def get_system_stats():
    """
    Get the current system statistics including CPU usage, CPU temperature,
    CPU model, RAM usage, total RAM, GPU usage, GPU memory usage, and total GPU memory.

    Returns:
        A dictionary containing the system statistics.
    """
    system_stats = {}

    try:
        system_stats["cpu_usage"] = psutil.cpu_percent()
        system_stats["cpu_freq"] = psutil.cpu_freq().current / 1000
        system_stats["cpu_model"] = cpuinfo.get_cpu_info()["brand_raw"]
        system_stats["ram_usage"] = psutil.virtual_memory().percent
        system_stats["total_ram"] = psutil.virtual_memory().total / (1024 ** 3)

        gpus = GPUtil.getGPUs()
        system_stats["gpu_usage"] = gpus[0].load * 100
        system_stats["gpu_memory_usage"] = gpus[0].memoryUtil * 100
        system_stats["total_gpu_memory"] = gpus[0].memoryTotal

    except Exception as e:
        system_stats["cpu_usage"] = 0
        system_stats["cpu_freq"] = 0
        system_stats["cpu_model"] = "N/A"
        system_stats["ram_usage"] = 0
        system_stats["total_ram"] = 0
        system_stats["gpu_usage"] = 0
        system_stats["gpu_memory_usage"] = 0
        system_stats["total_gpu_memory"] = 0

    return system_stats