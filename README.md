# OpenMonitor

<center>

![LineMode](https://github.com/Kannmu/OpenMonitor/blob/main/Img/LineMode.png)

LineMode

![TableMode](https://github.com/Kannmu/OpenMonitor/blob/main/Img/TableMode.png)

TableMode

</center>

OpenMonitor is a command line tool developed with Python that provides real-time system information and other information.

## Supported Information

The script retrieves the following system information:

- **CPU** : The current CPU usage and model name.
- **RAM** : The current RAM usage.
- **GPU** : The current GPU usage as a percentage, and usage of VRAM.
- **WiFi** : The **SSID** (network name), **RSSI** (in dBm and percentage).
- **Bluetooth BAT**: The battery life of supported devices that are paired to this computer.

## Usage

### Excusable File

Simply run `OpenMonitor.exe` or run through py script.

The lasted release is in [Here](https://github.com/Kannmu/OpenMonitor/releases)

### Run in script

To run the script, use the following command:

```
python OpenMonitor.py [-t]
```

The script accepts an optional argument `-t` or `--TablePrintInfo` to display the system information in a table format.

If no argument is provided, the script will display the system information in a line format.

The script continuously updates and refreshes the system information every 2 second and update Bluetooth BAT every 1min.

#### Dependencies

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.