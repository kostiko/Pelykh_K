# class MyClass():
#   '''This is second class'''
#   a = 10
#   def func(self):
#        print('Hello')
# print(MyClass.a)

# print(MyClass.func)

# print(MyClass.__doc__)
#--------------------------------------------------------------------------------------------------------------

# class A:
#     pass
# def myMethod (self, x):
#         return x * x
# A.m1 = myMethod
# A.attr1 = 2 * 2
#--------------------------------------------------------------------------------------------------------------

class Point:
    def __init__ (self, x, y, z):
        self.coord = (x, y, z)
    def __repr__ (self):
        return "Point (%s, %s, %s)" % self.coord
P = Point(0.0, 1.0, 0.0)
print(P)
#--------------------------------------------------------------------------------------------------------------
# class Person:
# # конструктор
#     def __init__(self, name):
#         self.name = name  # встановлюємо ім’я
#     def display_info(self):
#         print("Hello, my name is ", self.name)

# person1 = Person("Tom")
# person1.display_info()         # Hello, my name is Tom
# person2 = Person("Sam")
# person2.display_info()         # Hello, my name is Sam

#--------------------------------------------------------------------------------------------------------------
# class Line:
#      def __init__(self, p1, p2):
#          self.line = (p1, p2)
#      def __del__(self):
#          print ("Removing Line %s - %s" % self.line)
# L = Line((0.0, 1.0),(0.0, 2.0))
# Line.__del__(L)
#  #Removing Line (0.0, 1.0) - (0.0, 2.0)

# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b

#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print(v1 + v2)

# Vector (7, 8)

#--------------------------------------------------------------------------------------------------------------

# class Singleton(object):
#     obj=None # attribute for storing a single copy
#     def __new__(self, *args, **kwargs):
#          if self.obj is None:
#                # If it does not yet exist, then
#                # call __new__ of the parent class	
#                self.obj = object. __new__ (self, * args, ** kwargs)
#          return self.obj # will return Singleton

# obj_1 = Singleton()
# obj_1.Attr = 12
# new_obj = Singleton()
# print(new_obj.Attr)                       
 
# print(new_obj is obj_1) 
# print(new_obj and obj_1) #- is one and the same object

#--------------------------------------------------------------------------------------------------------------

# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b

#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
#    def __sub__(self,other):
#       return Vector(self.a - other.a, self.b - other.b)

# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print(v1 + v2)
# print(v1 - v2)

# Vector (7, 8)

#--------------------------------------------------------------------------------------------------------------

# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,3)  #super().__init__(3) 

#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)

# class Rectangle(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,2)  #super().__init__(3) 

#     def findArea(self):
#         a, b= self.sides
        
#         area = a*b
#         print('The area of the rectangle is %0.2f' %area)
# # t = Triangle()
# # t.inputSides()
# # t.dispSides()
# # t.findArea()

# r=Rectangle()
# r.inputSides()
# r.dispSides()
# r.findArea()

# class Parent(object):
#     def isParOrPChild(self):
#         return True
#     def who(self):
#         return 'parent'
# class Child (Parent):
#     def who (self):
#         return 'child'
# x = Parent()
# print(x.who(), x.isParOrPChild())
# x = Child()
# print(x.who(), x.isParOrPChild())

# class Parent(object):
#     def foo(self):
#         return 'who'
#     def foo(self, s):
#         return 'who ' + s
# x = Parent()
# print(x.foo("boo"))
# print(x.foo())


# #--------------------------------------------------------------------------------------------------------------
#
# class Class1:
#     def __init__(self):  # Конструктор класу
#         print("Called the method __init__()")
#     def __del__(self):  # Деструктор классу
#         print("Called the method __del__()")
# ################################################################        
# c1 = Class1()          # Виведе: Called the method __init__()
# # del c1                 # Виведе: Called the method __del__()
# c2 = Class1()          # Виведе: Called the method __init__()
# c3 = c2                # Створюємо посилання на екземпляр класу
# del c2                 # Ничого не виведе, так як існує посилання
# # del c3                 # Виведе: Called the method __del__()
#--------------------------------------------------------------------------------------------------------------
#
#1.  Створити клас машина з атрибутами name,  make, model та методами start та stop, 
#    які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.

# class Car:
#     def __init__(self,name,make,model):
#         self.name=name
#         self.make=make
#         self.model=model
#     def Start (self):
#         print("Car {} make {} model {} is started".format(self.name,self.make,self.model))
#     def Stop (self):
#         print("Car {} make {} model {} is stop".format(self.name,self.make,self.model))

# L=Car("Lexus","Japan","RX")
# L.Start()
# B=Car("BMW","Germany","E39")
# B.Stop()
#--------------------------------------------------------------------------------------------------------------
#
# Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення 
# “Hello, my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль,  
# в якому конструктор встановлює ім’я, а метод move виводить повідомлення

# class Person:
#     def __init__(self,name):
#         self.name=name

#     def Info (self):
#         print("Hello, my name is {}".format(self.name))
# P=Person(input("Name: "))
# P.Info()