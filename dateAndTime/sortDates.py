from datetime import date
import time

# Measure program runtime (start time)
startTime = time.perf_counter()

# Sort dates
ldates = []
d1 = date(2180,8,12)
d2 = date(2019,2,12)
d3 = date(2019,8,12)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.sort()

# Temporarily stop and delay the program
time.sleep(3)

for d in ldates:
    print(d)

# Measure program runtime (end time)
endTime = time.perf_counter()
print("Execution Time : ", endTime - startTime)