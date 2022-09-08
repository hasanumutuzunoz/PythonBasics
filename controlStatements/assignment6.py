#Print all numbers up to input number
#skip multiple of 10
#stop if the no > 100
x = int(input("Please enter a number"))
i = 0
while i < x:
    i += 1
    if (i%10 == 0):
        continue
    elif i>100:
        break
    else:
        print(i)



