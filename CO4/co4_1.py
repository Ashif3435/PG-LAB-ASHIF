class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        self.area=self.l*self.b
        self.p=2*(self.l+self.b)
    def display(self):
        print("AREA:",self.area)
        print("Perimeter:",self.p)

p1=Rectangle(3,4)
p2=Rectangle(5,6)
print("REACTANGLE 1")
p1.display()
print("REACTANGLE 2")
p2.display()

if p1.area>p2.area:
    print(" Rectangle with area ",p1.area,"is larger")
else:
    print(" Rectangle with area ",p2.area,"is larger")

