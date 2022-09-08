import time, datetime

# Print Seconds
epochSeconds = time.time()
print(epochSeconds)

# Print Current Date and time
t = time.ctime(epochSeconds)
print(t)

# Print Current Date and time
dt = datetime.datetime.today()
print(dt)
print("Current Date : {}/{}/{}".format(dt.day, dt.month, dt.year))
print("Current Time : {}:{}:{}:{}".format(dt.hour, dt.minute, dt.second, dt.microsecond))