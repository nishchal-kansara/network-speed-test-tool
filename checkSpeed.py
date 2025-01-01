import speedtest
import requests
from tqdm import tqdm
import time

def is_internet_available():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json", timeout=5)
        if response.status_code == 200:
            return response.json()["ip"]
    except requests.RequestException:
        pass
    return None

def get_location_info():
    try:
        public_ip = get_public_ip()
        if public_ip:
            response = requests.get(f"https://ipinfo.io/{public_ip}/json", timeout=5)
            if response.status_code == 200:
                location_info = {
                    "org": response.json().get("org"),
                    "city": response.json().get("city"),
                    "region": response.json().get("region"),
                    "country": response.json().get("country")
                }
                return location_info
    except requests.RequestException:
        pass
    return None

def check_speed():
    if not is_internet_available():
        print("Unable to connect to the network.")
        return

    st = speedtest.Speedtest()

    st.get_best_server()

    print("================================================")
    print("Network Information:")
    print("================================================")

    public_ip = get_public_ip()
    if public_ip:
        print(f"{public_ip}")
    else:
        print("Unable to get IP address.")

    location_info = get_location_info()
    if location_info:
        print(f"{location_info['org']}")
        print(f"{location_info['city']}, {location_info['region']}, {location_info['country']}")
    else:
        print("Unable to get Location.")

    # Proceed with the speed test as before
    print("\n================================================")
    print("Download Speed:")
    print("================================================")
    print("Download Speed (Progress Bar):")
    with tqdm(unit="Mbps", unit_scale=True) as progress_bar:
        download_speed = st.download()
        for _ in range(10):
            time.sleep(0.5)
            progress_bar.update(download_speed / 10 / 10**6)
        progress_bar.close()

    ds = download_speed / 10**6
    print(f"\nDownload Speed: {ds:.2f} Mbps")
    print(f"Download Speed: {ds*0.125:.2f} MBps")

    print("\n================================================")
    print("Upload Speed:")
    print("================================================")
    print("Upload Speed (Progress Bar):")
    with tqdm(unit="Mbps", unit_scale=True) as progress_bar:
        upload_speed = st.upload()
        for _ in range(10):
            time.sleep(0.5)
            progress_bar.update(upload_speed / 10 / 10**6)
        progress_bar.close()

    us = upload_speed / 10**6
    print(f"\nUpload Speed: {us:.2f} Mbps")
    print(f"Upload Speed: {us*0.125:.2f} MBps")

    print("\n================================================")
    print("Ping:")
    print("================================================")
    ping = st.results.ping
    print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
    check_speed()