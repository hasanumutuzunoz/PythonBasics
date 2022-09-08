s= "   You are awesome    "
print(s)

s1="""You are
the creator 
of your destiny"""
print(s1)

print(s[0]) #print first character
print(s*3) #print 3 times
print(len(s1)) #print the length
print(s[0:5])
print(s[0:])
print(s[:8])
print(s[-3:-1])

print(s[0:9:2]) #print characters with 2 steps jump forward
print(s[15::-1]) #print characters with 1 step jump backward
print(s[::-1])  #same

print(s.strip()) #remove spaces at the begining and ending function
print(s.lstrip()) #remove left spaces
print(s.rstrip()) #remove right spaces

print(s.find("awe", 0, len(s))) #search string from  0 to lenght
print(s.find("awe", 0, 8)) #-1 cannot find it
print(s.count("a")) #count strings
print(s.replace("awesome","super")) #replace strings
print(s.strip().replace("awesome","super").upper()) #use multiple functions at the same time

print(s.upper()) #print all upper case
print(s.lower()) #print all lower case
print(s.title()) #print first letters upper