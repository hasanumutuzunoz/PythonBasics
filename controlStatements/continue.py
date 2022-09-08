#skip the multiples of 3 with continue
x=0
while x<20:
    x += 1
    if x%3 == 0:
        continue
    print(x)
