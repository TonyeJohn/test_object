class Polygon:
    def __init__(self,sides):
        self.sides=sides
        
    def display_info(self):
         print('A polygon is a two dimensional shape with straight lines')
         
    def get_perimeter(self):
         perimeter= sum(self.sides)
         print('Perimeter: ',perimeter)
         return perimeter
         
class Triangle(Polygon):
     def display_info(self):
         print('A triangle is a polygon with 3 sides')
         Polygon.display_info(self)#method overriding
        
class Quadrilateral(Polygon):
        def display_info(self):
            print('A quadrilateral is a polygon with 4 sides')
            super().display_info()#right method overriding

t1=Triangle([3,4,5])
t1.get_perimeter()
t1.display_info()

q1=Quadrilateral([3,4,5,6])
q1.get_perimeter()
q1.display_info()