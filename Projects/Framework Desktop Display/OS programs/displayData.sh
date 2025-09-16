#!bin/bash

#Set the port and baud rate
PORT="/dev/ttyACM0"
BAUD=38400

#Open the port and keep it open while the script is running
stty -F "$PORT" $BAUD cs8 -cstopb -parenb -crtscts -ixon -ixoff -echo raw
exec 3>"$PORT"

#Main While loop
while true; do

#Fetch maximum memory
memmax=$(grep MemTotal /proc/meminfo | awk '{print $2}')
memmax=$((memmax / 1024))
#echo "$memmax"

#Fetch avaliable memory
memavail=$(grep MemAvailable /proc/meminfo | awk '{print $2}')
memavail=$((memavail / 1024))
#echo "$memavail"

#calculate used memory based on max and avaliable
memused=$((memmax - memavail))
#echo "$memused"

#Fetch cpu temp from sensors
cputemp=$(< /sys/class/thermal/thermal_zone0/temp)
cputemp=$(echo "scale=1; $cputemp / 1000" | bc -l)
#echo "$cputemp"

#Send data out to COM port and sleep
echo -n "$(($memmax))P$(($memused))P$(($memavail))P${cputemp}P999P999PE" >&3
sleep 1
done
