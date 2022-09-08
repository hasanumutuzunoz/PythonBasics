id=1
firstName = "John"
lastName = "            Bailey"
ssn = "374-12-847"
hasInsurance = True
billingAmound = "1000"

print(type(billingAmound))
billingAmound = float(billingAmound)  #convert str to float
print(type(billingAmound))

print(id, firstName, lastName.lstrip(), ssn, hasInsurance, billingAmound, ssn[7:len(ssn)])


#For constant variables use CAPITAL names
COUNTRY = "Canada" #constant variable - do not change
INTEREST_RATE = 7
print(COUNTRY)

