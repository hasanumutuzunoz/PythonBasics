lst = [1, 2, 3, 40, 87]
# Filter function has 2 parameters,
# Filter first parameter is lambda function, second is the list
# Return only even numbers
# If first parameter is true, then return it from the list
# Very useful when we retrieve data from database to filter
result = list(filter(lambda x : x%2==0, lst))
print(result)
for i in result: print(i)