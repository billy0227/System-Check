import psutil
import os.path
import os

if not os.path.exists('C:\System Information Dump'):
    os.makedirs('C:\System Information Dump')

save_path = 'C:\System Information Dump'
file_name = "System Info Dump.txt"


completeName = os.path.join(save_path, file_name)
file1 = open(completeName, "w")



# Measure cpu times-----------------------------------


def montior_cpu_times():
    file1.write("\nCPU TIMES\n")
    cpu_times = psutil.cpu_times()
    user_time = round(cpu_times.user/3600)
    system_time = round(cpu_times.system/3600)
    idle_time = round(cpu_times.idle/3600)
    file1.write(str("Time spent on processes by the User: {} Hours \n".format(user_time)))
    file1.write(str("Time spent on processes by the System: {} Hours\n".format(system_time)))
    file1.write(str("Time spent on processes by the idle: {} Hours\n".format(idle_time)))

# Measure CPU util-------------------------------------


def monitor_cpu_util():
    file1.write("\nCPU UTIL\n")
    file1.write(str(psutil.cpu_percent()))

# Count CPU cores--------------------------------------


def monitor_cpu_cores():
    file1.write("\n\nCPU CORES\n")
    file1.write(str(psutil.cpu_count()))

# Measure CPU frequencies-------------------------------


def monitor_cpu_freq():
    file1.write("\n\nCPU FREQUENCIES\n")
    file1.write(str("{} Mhz".format(psutil.cpu_freq().current)))

# Monitor RAM Usage-------------------------------------


def monitor_RAM_Usage():
    file1.write("\n\nRAM USAGE")
    virtual_memory = psutil.virtual_memory()
    file1.write(str("Total Memory {}GB\n".format(str(round(virtual_memory.total / (1024.0 ** 3))))))
    file1.write(str("Available Memory {}GB\n".format(
        round(virtual_memory.available / (1024.0 ** 3)))))
    file1.write(str("Used Memory {}GB\n".format(round(virtual_memory.used / (1024.0 ** 3)))))
    file1.write(str("Percentage Memory {}%\n".format(virtual_memory.percent)))
    
# Monitor disk partitions


def monitor_disk():
    file1.write("\nDISK PARTITIONS\n")
    file1.write(str(psutil.disk_partitions()))

# Disk Utilization


def monitor_disk_usage():
    file1.write("\nDISK USAGE C:\n")
    disk_usage = psutil.disk_usage('C:')
    file1.write(str("Total Memory {}GB\n".format(round(disk_usage.total / (1024.0 ** 3)))))
    file1.write(str("Free Memory {}GB\n".format(round(disk_usage.free / (1024.0 ** 3)))))
    file1.write(str("Used Memory {}GB\n".format(round(disk_usage.used / (1024.0 ** 3)))))
    file1.write(str("Percentage Memory {}%\n".format(disk_usage.percent)))

    file1.write("\nDISK USAGE D:\n")
    disk_usage = psutil.disk_usage('D:')
    file1.write(str("Total Memory {}GB\n".format(round(disk_usage.total / (1024.0 ** 3)))))
    file1.write(str("Free Memory {}GB\n".format(round(disk_usage.free / (1024.0 ** 3)))))
    file1.write(str("Used Memory {}GB\n".format(round(disk_usage.used / (1024.0 ** 3)))))
    file1.write(str("Percentage Memory {}%\n".format(disk_usage.percent)))


# Monitor network requests


def monitor_network():
    file1.write("\nNETWORK REQUESTS\n")
    io_stats = psutil.net_io_counters()
    file1.write(str("Total Bytes Sent {} \n".format(io_stats.bytes_sent)))
    file1.write(str("Total Bytes Received {} \n".format(io_stats.bytes_recv)))

# Run all checks


def run_all_checks():
    montior_cpu_times()
    monitor_cpu_util()
    monitor_cpu_cores()
    monitor_cpu_freq()
    monitor_RAM_Usage()
    monitor_disk()
    monitor_disk_usage()
    monitor_network()
    
run_all_checks()

# def file1():
# return run_all_checks()
#info = file1()
#file = open("System Info Dump.txt","a")
# file.write(str(info))
# file.close()
# file1()
