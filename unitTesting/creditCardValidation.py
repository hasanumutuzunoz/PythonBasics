from datetime import *

def validateCard(expDate):
    if expDate > datetime.now().date():
        return 'Valid'
    else:
        raise RuntimeError('Car has expired')


#print(validateCard(date(2022,2,2)))