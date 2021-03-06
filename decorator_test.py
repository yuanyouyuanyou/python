def decorator(F):
    def new_F(a,b):
        print "input:"
        print a,b
        return F(a,b)
    return new_F

@decorator
def square_sum(a,b):
    return a**2 + b**2

print(square_sum(3,4))

"""
def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()

output:
('total display', 1)
('My age is', 5)
('total display', 2)
('My age is', 5)
('total display', 3)
('My age is', 5)
"""
