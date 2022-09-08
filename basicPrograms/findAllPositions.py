s = "Take up one idea and make that idea your life. "
    "Think and dream of that idea and leave every other idea alone."
print(s)

subs = "idea"
found = False
pos = -1
lenght = len(s)
while True:
    pos = s.find(subs, pos+1, lenght)
    if pos == -1:
       break
    print("Found the sub string at the position ", pos)
    found = True
if found == False:
    print("Sub String not found")