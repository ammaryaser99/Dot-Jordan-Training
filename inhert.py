class circle:
    r:int
    def __init__(self ,r):
        self.r=r
    def get_area(self):
        print(3.14*(self.r**2))
class clinder(circle):
    h:int
    def __init__(self, r,h):
        self.r=r
        self.h=h
        

c1=clinder(5,10)
c1.get_area()