import serial, os, sys, datetime, time

comments = input("Sample?  ").replace(' ', '_')
basefilename = datetime.datetime.now().strftime("%Y%m%dT%H%M%S") + "_" + comments
csvfilename = basefilename + "_DATA.csv"
statfilename = basefilename + "_STAT.txt"
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
ser = serial.Serial(port, 115200, timeout=1)

start_time = time.time()
statfile.write(str(start_time) + "\n")
t1 = 300  # 5 minutes  300
# t2 = 3900  # 65 minutes   3900
t2 = 30*60 + t1  # 30 minutes of dissolution

# measurement_number = 0
ser.flush()
ser.read_all()
while True:
    et = time.time() - start_time
    if 0 <= et < t1:
        print(f"{str(datetime.timedelta(seconds=t1-et))}", end="\t")
    elif t1 <= et < t2:
        print(f"{str(datetime.timedelta(seconds=t2-et))}", end="\t")
    if et >= t2:  # was elif
        break
    s = ser.readline().decode("utf-8", "ignore")
    # if(measurement_number % 10000 == 0):
    #     print(f"{str(datetime.timedelta(seconds=t1-et))}\t{ser.inWaiting()}\t{s}", end="")
    # measurement_number += 1
    print(f"{ser.inWaiting()}\t{s}", end="")

    csvfile.write(s)


statfile.write(str(time.time()) + "\n")
csvfile.close()
statfile.close()
