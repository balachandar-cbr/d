# Ex 3: Latency, Bandwidth and Throughput
print("Network Performance Analysis")
latency = float(input("Enter latency (ms): "))
bandwidth = float(input("Enter bandwidth (Mbps): "))
data_size = float(input("Enter data transferred (MB): "))
time = float(input("Enter transfer time (seconds): "))

throughput = data_size / time  # MB/s

print("\n----- Results -----")
print("Latency :", latency, "ms")
print("Bandwidth :", bandwidth, "Mbps")
print("Throughput:", round(throughput, 2), "MB/s")

if throughput * 8 <= bandwidth:
    print("Throughput is within the available bandwidth.")
else:
    print("Throughput exceeds the specified bandwidth.")

if latency < 50:
    print("Latency Status: Low")
elif latency <= 100:
    print("Latency Status: Moderate")
else:
    print("Latency Status: High")
