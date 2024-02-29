class Multiplex:
    tickets = 300
    mainobj = None
    def __new__(cls):
        if cls.mainobj is None:
            cls.mainobj = super().__new__(cls)
        return cls.mainobj
    
    def animal(self):
        ticket = int(input('Ticket for animal:'))
        if ticket < self.tickets:
            self.tickets -= ticket
            print('Remaining:',self.tickets)
        else:
            print('tickets are full')

    def chichore(self):
        ticket = int(input('Ticket for chichore:'))
        if ticket < self.tickets:
            self.tickets -= ticket
            print('Remaining:',self.tickets)
        else:
            print('tickets are full')

obj1 = Multiplex.__new__(Multiplex)
print(obj1)
obj1.animal()
obj1.chichore()

obj2 = Multiplex.__new__(Multiplex)
print(obj2)
obj2.animal()
obj2.chichore()
