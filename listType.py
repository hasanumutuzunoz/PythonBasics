lst=[10,20, "Hasan", -10, 30.5]
print(lst)
print(lst[-3])
print(lst[3:5])
print(lst*4)
print(len(lst))

lst.append(40) #Add element to the list
print(lst)
lst.remove("Hasan") #remove element from the list by name
print(lst)
del(lst[1]) #remove element from the list by index
print(lst)

#lst.clear() #clear all elements
#print(lst)

print(max(lst)) #print max element
print(min(lst)) #print min element

lst.insert(3, 99) #insert element to specific location
print(lst)

lst.sort() #sort list
print(lst)

lst.sort(reverse=True) #reverse sort
print(lst)


