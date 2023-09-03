class Car():
    name:str
    model:str
    color:str
    price:float
    def discount(self,per):
        self.price-=self.price*per
        print(self.price)
    def __init__(self,name,price):
        self.name=name
        self.price=price
car1=Car('Mazda',15000)
car1.name='Ford'
car1.model='Fusuion'
car1.color='Black'
car1.price=10000
car1.discount(0.04)
