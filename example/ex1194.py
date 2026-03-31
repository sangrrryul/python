class blackbox:
      pass
    
b1=blackbox()
b1.name='까망이'
print(b1.name)
print(isinstance(b1, blackbox))


# -------------------------------------

class Blackbox:
    def __init__(self,name, price):
        self.name = name
        self.name = price

b1 = Blackbox('까망이', 200000)  
print(b1.name, b1.price)      
b2 = Blackbox('하양이', 100000)
print(b2.name,b2.price)