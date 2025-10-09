import psutil
import serial
import time
import wmi

# WMI interface
w = wmi.WMI(namespace="root\\CIMV2")

# Serial to ESP32
ser = serial.Serial("COM14", 115200)  # change COM port if needed
time.sleep(0.25)
print("setup complete")

while True:
    # CPU + RAM
    cpu = int(psutil.cpu_percent(interval=None))
    ram = int(psutil.virtual_memory().percent)

    # GPU utilization (AMD supported via WMI PerfMon counters)
    gpu = 0
    for gpu_instance in w.Win32_PerfFormattedData_GPUPerformanceCounters_GPUEngine():
        if "engtype_3D" in gpu_instance.Name:  # 3D engine load
            gpu += int(gpu_instance.UtilizationPercentage)

    #Sometimes gpu util fetches >100% util
    if(gpu > 100):
        gpu = 100
        
    # Send CSV
    data = f"{cpu},{ram},{gpu}\n"
    ser.write(data.encode())
    print("fetch complete")

    time.sleep(0.25)