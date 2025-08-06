# # del to delete obj
 
# class Student:
#     def __init__(self, name):
#         self.name = name
    
# s1 = Student("dhruv")
# print(s1.name)

# del s1.name

# print(s1.name)


#####################################
# private attribute & methods 
###################################

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         # for private attributes
#         self.__acc_pass = acc_pass
    
#     # it not private call methods and print value 
#     def reset_pass(self):
#         print(self.__acc_pass)

#     def __hello(self):
#         print("this is private")

#     def welcome(self):
#         self.__hello()

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)

# print()
# acc1.reset_pass()

# print()

# acc1.welcome()


#######################################
# inheritance
#######################################
# single 
# class Car:
    
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stop..")


# class ToyotaCar(Car):

#     def __init__(self, brand, type):
#         # super method 
#         super().__init__(type)
#         self.brand = brand
#         super().start()


# car1 = ToyotaCar("dhruv", "petrol")

# print(car1.type)


# multi-level
# class type_car(ToyotaCar):
#     def __init__(self, type):
#         self.type = type


#car1=type_car("petrol")

#print(car1.start())


######################
# multiple
######################
# class A:
#     var1="dhruv"

# class b:
#     var2="raju"

# class c(A,b):
#     var3="welcome to c"

# c1 = c()

# print(c1.var2)

##################
# super method
#################


########################
# class method
########################

# class person:
#     name = "ano"

#     # class method 
#     @classmethod
#     def c_name(cls, name):
#         # method 1 to change name
#         # person.name = name

#         # method 2 to change name
#         # self.__class__.name = "dhruv"
#         cls.name = name


# p1 = person()

# p1.c_name("raju kumar")
# print(p1.name)
# print(person.name)

############################
# property decorator
############################
# class Student:

#     def __init__(self, phy, chm, math):
#         self.phy = phy
#         self.chm = chm
#         self.math = math
#         #self.per = str((self.phy + self.chm + self.math) / 3) + "%"

#     @property
#     def per(self):
#         return str((self.phy + self.chm + self.math) / 3) + "%"

#     # def cal_per(self):
#     #     self.per = str((self.phy + self.chm + self.math) / 3) + "%"

# stu1 = Student(11,33,44)

# print(stu1.per)

# stu1.phy = 88

# print(stu1.phy)
# print(stu1.per)


##################
# polymorphism
##################

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def ShowNumber(self):
#         print(self.real,"i+",self.img,"j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

# num1= Complex(1,4)

# num1.ShowNumber()

# num2= Complex(2,4)

# num2.ShowNumber()

# # dunder fun

# num3 = num1 + num2

# num3.ShowNumber()

# c = num1 - num2

# c.ShowNumber()


######################
# practice

# q1 define a circle class create a circle with radius r using the constructor
# define an area() method of the class which calculates the area of the circle
# define a perimeter() method of the class which allows you to calculate the parimeter of the circle

# q2 define a employee class with attribute role, department, alary this class also has showdetails() method
# create an engineer class that inherits properties form employee &  has additional attributes: name & age


# create a class called order which store item & it price
# use dunder function __gt__() to convert that:
# order1 > order2 if price of order > price of order2