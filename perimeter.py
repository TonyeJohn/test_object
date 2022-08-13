class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        p=self.a+self.b+self.c
        return p
t1=Triangle(3,4,5)
p=t1.perimeter()
print('Perimeter: ', p)