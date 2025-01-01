# Network Speed Test Tool

This Python script allows you to test the internet speed (download, upload, and ping) and gather basic information about your network connection. It also provides details about your public IP address and geographical location based on the IP.

## Features

- **Network Availability Check**: Verifies whether the internet connection is available.
- **Public IP Address**: Retrieves and displays your public IP address.
- **Location Information**: Fetches and displays your geographical location (city, region, country, and ISP).
- **Speed Test**:
  - Download speed (Mbps and MBps)
  - Upload speed (Mbps and MBps)
  - Ping (latency in milliseconds)
- **Progress Bars**: Displays progress bars while measuring download and upload speeds.

## Requirements

Before running the script, ensure that you have the following Python libraries installed:

- `speedtest-cli` - For measuring internet speed.
- `requests` - For making HTTP requests to fetch public IP and location info.
- `tqdm` - For displaying progress bars during download/upload speed measurements.

You can install the required libraries using following commands:

```bash
pip install speedtest-cli requests tqdm
```
or
```bash
 python3 -m pip install speedtest-cli requests tqdm
```

## Run this Python Script using Following Commands:
1. ```bash
   cd {project_directory}
   ```
2. ```bash
   python3 checkSpeed.py
   ```

   or
   
   ```bash
   cd {project_directory} & python3 checkSpeed.py
   ```

## Demo Network Speed Test Tool:
![Network Speed Test Tool](https://github.com/user-attachments/assets/233b0bd7-9477-4968-806d-a05a5880e737)
