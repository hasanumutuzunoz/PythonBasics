"""
I made some upgrades and used 2 while loops here. For the question do you want to kow the salary of another person.
If the answer is Yes, then break first loop and go back to second loop
If the answer is No, then break both loops
If the answer is not Yes or No, then ask the question again.
Simple :)
"""

n = int(input("enter the number of employees"))
employees = {}
for i in range(n):
    name = input("Enter the employee name")
    salary = input("Enter the employee salary")
    employees[name] = salary
print("You can know the salary details by entering the names")
firstLoop = True
secondLoop = True
while firstLoop:
    name = input("Enter employee name")
    salary = employees.get(name, -1)
    if salary == -1:
        print("Employee does not exist")
    else:
        print("The salary of the employee is ", salary)

    while secondLoop:
        choice = input("Do you want to know the salary of another employee? [Yes|No]")
        if choice == "No":
            firstLoop = False
            break
        elif choice != "Yes":
            print("Invalid Input. Please enter \"Yes\" or \"No\"")
        else:
            break




