# OpenMonitor

OpenMonitor is a Python script that provides real-time system information such as CPU usage, CPU temperature, CPU model, RAM usage, total RAM, GPU usage, GPU memory usage, total GPU memory, system power consumption, and WiFi network information. The script uses various libraries such as `os`, `psutil`, `cpuinfo`, `GPUtil`, `time`, `pywifi`, `numpy`, `prettytable`, and `argparse` to gather and display the system information.

## System Information

The script retrieves the following system information:

- CPU Usage: The current CPU usage as a percentage.
- CPU Model: The CPU model name.
- RAM Usage: The current RAM usage as a percentage.
- Total RAM: The total RAM of the system in gigabytes.
- GPU Usage: The current GPU usage as a percentage.
- GPU Memory Usage: The current GPU memory usage as a percentage.
- Total GPU Memory: The total GPU memory in bytes.
- WiFi Network Information: The SSID (network name), signal strength (in dBm and percentage), and authentication protocol of the currently connected WiFi network.

## Usage

To run the script, use the following command:

```
python openmonitor.py [-t]
```

The script accepts an optional argument `-t` or `--TablePrintInfo` to display the system information in a table format.

If no argument is provided, the script will display the system information in a line format.

The script continuously updates and refreshes the system information every second.

## Dependencies

The script requires the following dependencies:

- `psutil`: Used to retrieve CPU and RAM information.
- `cpuinfo`: Used to retrieve CPU model information.
- `GPUtil`: Used to retrieve GPU information.
- `pywifi`: Used to retrieve WiFi network information.
- `prettytable`: Used to display the system information in a table format.
- `argparse`: Used to parse command-line arguments.

You can install the dependencies using the following command:

```
pip install psutil cpuinfo gputil pywifi prettytable argparse
```

## Output

The script outputs the system information in the following format:

### Line Format

```
CPU: <CPU Usage>% <CPU Frequency>GHz <CPU Model>
RAM: <RAM Usage>% (<Used RAM>/<Total RAM>)
GPU: <GPU Usage>% (<Used GPU Memory>/<Total GPU Memory>)
WI-FI: <SSID> <Signal Strength>dBm <Signal Strength Percentage>%
```

### Table Format

```
+-------+--------+-------+
|  Item | Usage  | Total |
+-------+--------+-------+
|  CPU  | <CPU Usage>% | <CPU Frequency>GHz |
|  RAM  | <RAM Usage>% | <Used RAM>/<Total RAM> |
|  GPU  | <GPU Usage>% | <Used GPU Memory>/<Total GPU Memory> |
| WI-FI | <SSID> | <Signal Strength>dBm |
+-------+--------+-------+
```

## Example

To display the system information in a table format, run the following command:

```
python openmonitor.py -t
```

To display the system information in a line format, run the following command:

```
python openmonitor.py
```

The script will continuously update and refresh the system information every second.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.