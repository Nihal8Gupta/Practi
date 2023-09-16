class supermarket:
    s_name='DMART'
    s_product={'Kurkre':10,'Good day':10,'Coke':20,'Tea':15,'Bingo':20}
    def __init__(self,n,o=123):
        self.name=n
        self.orderId=o
    def purchase(self):
        print('\nProduct List :-')
        for k,v in self.s_product.items():
            print(k,'Rs-',v)
        self.orderlist={}
        print('For cencel type :','exit')
        while True:
            t=input('Enter the product name as in list/exit')
            if t in self.s_product:
                pcs=int(input(f'Quantity for {t}:'))
                if t not in self.orderlist:
                    self.orderlist[t]=pcs
                else:
                    self.orderlist[t]=self.orderlist[t]+pcs
            else:
                return len(self.orderlist)
    def payment(self):
        self.total=0
        print('\nPayable Bill:-')
        print('Customer name',self.name)
        print('Order Id',self.orderId)
    
        for k,v in self.orderlist.items():
            print(k,'Qnt-',v,'Price-',v*self.s_product[k])
            self.total+=v*self.s_product[k]
        print('Total Amount :',self.total)
print('Welcome to',supermarket.s_name)
name=input('Enter your name:')
print('THANK YOU FOR COMING!')
obj=supermarket(name)            
q=input('You want to Purchase\nplz enter YES:')
if q in ('YES','yes'):
    n=obj.purchase()
    if n!=0: 
        obj.payment()