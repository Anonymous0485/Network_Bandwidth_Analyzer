import psutil
import time

def get_bytes_sent_and_received():
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_received = net_io_counters.bytes_recv
    return bytes_sent, bytes_received

def calculate_bandwidth(bytes_sent, bytes_received, interval):
    time.sleep(interval)
    new_bytes_sent, new_bytes_received = get_bytes_sent_and_received()
    sent_bandwidth = (new_bytes_sent - bytes_sent) / interval
    received_bandwidth = (new_bytes_received - bytes_received) / interval
    return sent_bandwidth, received_bandwidth

def main():
    interval = 1  # Interval in seconds
    while True:
        bytes_sent, bytes_received = get_bytes_sent_and_received()
        sent_bandwidth, received_bandwidth = calculate_bandwidth(bytes_sent, bytes_received, interval)
        print(f"Sent bandwidth: {sent_bandwidth:.2f} bytes/s")
        print(f"Received bandwidth: {received_bandwidth:.2f} bytes/s")
        print("-" * 30)
        time.sleep(1)

if __name__ == "__main__":
    main()
