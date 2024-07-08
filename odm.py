import serial, os, sys, datetime, time

comments = input("Sample?  ").replace(' ', '_')
csvfilename = datetime.datetime.now().strftime("%Y%m%dT%H%M%S") + "_" + comments + ".csv"
statfilename = csvfilename[:-4] + "_STAT.txt"
csvfile = open(csvfilename, "w")
statfile = open(statfilename, "w")
port = ""
usb_count = 0
devices = os.listdir("/dev")
for device in devices:
    if "cu.usb" in device:
        port = device
        usb_count += 1
if usb_count == 0:
    sys.exit("No port found")
if usb_count > 1:
    sys.exit("Multiple ports found")
port = "/dev/" + port
print(port)
data = []
ser = serial.Serial(port, 2000000, timeout=1)

start_time = time.time()
statfile.write(str(start_time) + "\n")
t1 = 300  # 5 minutes  300
t2 = 3900  # 65 minutes   3900

ser.flush()
while True:
    et = time.time() - start_time
    if 0 <= et < t1:
        print(f"{str(datetime.timedelta(seconds=t1-et))}", end="\t")
    elif t1 <= et < t2:
        print(f"{str(datetime.timedelta(seconds=t2-et))}", end="\t")
    elif et >= t2:
        break
    s = ser.readline().decode("utf-8", "ignore")
    print(ser.inWaiting(), end="\t")
    csvfile.write(s)
    print(s, end="")

statfile.write(str(time.time()) + "\n")
csvfile.close()
statfile.close()
