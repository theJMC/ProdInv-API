# TheJMC's ID Library. For More Details and Documentation go to https://github.com/TheJMC/JMC-ID
# Version 1.0

class ID: 
    def __init__(self, ident: str):
        # Check if Numerical
        for item in list(ident):
            try:
                int(item)
            except TypeError as e:
                raise Exception("Not All Integers") from e

        # Check if 8 Nums
        if len(ident) < 8:
            raise Exception("Too Short")
        elif len(ident) > 8:
            raise Exception("Too Long")

        # Set self.ident to the ID number
        self.id = ident
        
    def __str__(self):
        return self.id

    def __repr__(self):
        return f'ID({self.id})'

def generateID():
    import random
    import string

    digits = string.digits
    ident = ''.join(random.choice(digits) for i in range(8))
    return ID(ident)
