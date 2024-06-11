class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    
    def displaybikes(self):
        print("totol bikes:",self.stock)

    def rentforbike(self,q):
        
        if q <=0:
            print("enter the positive value")

        elif q >self.stock:
            print("enter the value less than stock")

        else:
            self.stock=self.stock-q
            print("total price ",q*100)
            print("total bikes",self.stock)

while True:
    obj=bikeshop(100)
    uc = int(input('''
    1.Display stock               
    2.rent a bike               
    3.exit        '''))

    if uc ==1:
        obj.displaybikes()
    
    elif uc ==2:
        n=int(input("Enter the qty:"))
        obj.rentforbike(n)
    
    else:
        break