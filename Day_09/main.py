# class Student:
#     # name = "dhruv"

#     # default constructor
#     # def __init__(self):
#     #     pass
#     #     print("new thing add...")

#     college_name="ppsu"

#     # parameterized  constructor
#     def __init__(self, f_name, marks):
#         print("new thing add...")
#         self.f_name = f_name
#         self.marks = marks

# # instance attribute 
# s1 = Student("dhruv", 55)
# print(s1.f_name, s1.marks)

# # using for diff value 
# # s2 = Student("raju", 56)
# # print(s2.f_name, s2.marks)

# # # both way access 
# # print(s2.college_name)
# # # for class attribute
# # print(Student.college_name)

##################################################
#                    class methods
##################################################
# class Student:
#     college_name="ppsu"

#     # parameterized  constructor
#     def __init__(self, f_name, marks):
#         self.f_name = f_name
#         self.marks = marks

#     # class methods
#     def hello(self):
#         print("hello",self.f_name)

#     def get_marks(self):
#         return self.marks

# s1=Student("dhruv", 66)
# # method call 
# s1.hello()

# print(s1.get_marks())

##################################################
# practice: create class that take name & mark of 3 sub as argument in constructor.
# then create a method to print the avg.
##################################################

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)

#     # methods
#     def get_ave(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("your marks is:", sum/3)



# s1=Student("dhruv", [22,23,55])

# s1.get_ave()



################################################
#                static method                 #
################################################

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)

#     # static method not need pass parameters
#     @staticmethod # it decorator 
#     def hello():
#         print("hello i am static methods")

#     # methods
#     def get_ave(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("your marks is:", sum/3)



# s1=Student("dhruv", [22,23,55])

# s1.get_ave()

# s1.hello()


####################################
#            abstractions          #
####################################
# it car class
# class Car:

#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clu = False

#     # in background user not see value
#     def start(self):
#         self.clu = True
#         self.acc = True
#         print("clutch pressed and car started")

#     def stop(self):
#         self.brk = True
#         print("car is stop")


# car1 = Car()
# car1.start()


######################################
# create account class with 2 attribute balance & account no.
# create methods for debit, credit & printing the current balance.
######################################

