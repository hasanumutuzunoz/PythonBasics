# Compare user input expiry date with current date to check if the credit card expired
from datetime import *
def validateCard(expDate):
    if expDate > datetime.now().date():
        print("Valid")
    else:
        print("Expired")

validateCard(date(2030,3,2))