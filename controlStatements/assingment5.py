grades = [int(x) for x in input("Enter you Maths, Physics, Chemistry grades. ").split()]

average = (grades[0] + grades[1] + grades[2])/3
print("You average score is:", average)

if grades[0] and grades[1] and grades[2] < 35: print("You have failed the exam")
elif average<= 59: print("Your grade is C")
elif average<=69: print("Your grade is B")
else: print("Your grade is A")
