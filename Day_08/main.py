# class student:
#     collge_name="abc"

#     def __init__(self, f_name, mark):
#         self.name = f_name
#         self.mark = mark
        
#     def hello(self):
#         print("welcome student", self.name)
    
#     def get_mark(self):
#         return self.mark


# s1 = student("dhruv", 44)

# s1.hello()

# print(s1.get_mark())
# # instance or class call
# data = student("dhruv", 55)
# print(data.name, data.mark)

# # print(data)

# data_2=student("raju", 44)
# print(data_2.name, data_2.mark)

# # this called class.attribute which come common obj 
# print(student.collge_name)
# class car:
#     color="blue"

# car1=car()

# print(car.color)

# create student class that take "name" "mark" = 3 stubject as argument constructor then create methid to print the average


# class student_list:

#     def __init__(self, name, mark):
#         self.name = name
#         self.marks = mark       

#     @staticmethod
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("you", self.name, "avg is:", sum/3)



# s1 = student_list("dhruv", [99, 99, 33])

# s1.get_avg()

# s1.hello()


# create account class with 2 attributes - balance & account no.
# create methods for debit, credit & print the balance

# class account:

#     def __init__(self, balance, account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def credit(self, amount):
#         self.balance += amount
#         print("RS.", amount ,"was credit")
#         print("total balance:", self.get_bal())

#     def debit(self, amount):
#         self.balance -= amount
#         print("RS.", amount ,"was debited")
#         print("total balance:", self.get_bal())

#     def get_bal(self):
#         return self.balance

# acc1 = account(10000, "A1")

# print(acc1.balance, acc1.account_no)

# acc1.credit(100)

# acc1.debit(2222)

# class student:
#     def __init__(self, name):
#         self.name = name

    

# s1 = student("dhruv")

# del s1

# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         # __ using this it get passwd
#         self.__acc_pass = acc_pass


# acc1 = account("1234", "abcde")


# print(acc1.acc_no)



# class person:

#     name = "ano"

#     # method 1
#     # def changeName(self, name):
#     #     self.__class__.name = "dhruv"
#     # method 2
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name


# p1 = person()

# p1.changeName("dhruv raju")

# print(person.name)


class student:
    def __init__(self, phy, chem, meth):
        self.phy = phy
        self.chem = chem
        self.meth = meth
        #self.perce = str((self.phy + self.chem + self.meth) / 3) + "%"

    
    # def calculator_final(self,):
    #     self.perce = str((self.phy + self.chem + self.meth) / 3) + "%"

    @property
    def perce(self):
        return str((self.phy + self.chem + self.meth) / 3) + "%"

stu1 = student(55,66,77)

print(stu1.perce)

