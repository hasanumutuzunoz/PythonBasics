import sys

lst = sys.argv
accBalance = 10000

if int(lst[1]) == 1:
    print("Account Balance: ", accBalance)
elif int(lst[1]) == 2:
    withdrawAmound = int(input("How much would you like to withdraw?"))
    accBalance = accBalance - withdrawAmound
    print("You withdraw : ", withdrawAmound, "dollars")
    print("Your account balance is : ", accBalance)
elif int(lst[1]) == 3:
    depositAmound = int(input("How much would you like to deposit?"))
    accBalance = accBalance + depositAmound
    print("You deposit : ", depositAmound, "dollars")
    print("Your account balance is : ", accBalance)
elif int(lst[1]) == 4:
    depositAmound = int(input("How much would you like to deposit with check?"))
    accBalance = accBalance + depositAmound
    print("You deposit : ", depositAmound, "dollars")
    print("Your account balance is : ", accBalance)
