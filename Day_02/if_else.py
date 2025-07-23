# # this is conditional statements

# light = "green"

# if light == "red":
#     print("you have to stop")
# elif light == "yellow":
#     print("you have to wait")
# elif light == "green":
#     print("you have to go")
# else:
#     print("light not define")

# indentation called with give space form start line 


# give mark based on grade 

# mark=int(input("enter your makr i will give grade:"))

# if mark >= 90:
#     print("you get grade A")
# elif mark >= 80 and mark < 90:
#     print("you get grade B")
# elif mark >= 70 and mark < 80:
#     print("you get grade C")
# else:
#     print("you get grade D")


# neting if in if 

# age = 90

# if age >= 18:
#     if age >= 80:
#         print("you are old my buddy")
#     else:
#         print("can drive")
# else:
#     print("not drive")


# check number is odd or even

# num=float(input("enter the number:"))


# if num%2 == 1:
#     print("number is odd")
# elif num%2 == 0:
#     print("number is even")
# else:
#     print("not number found")



# a=float(input("enter the number a:"))
# b=float(input("enter the number b:"))
# c=float(input("enter the number c:"))

# if a >= b and a >= c:
#     print("a is greater", a)
# elif b >= c:
#     print("b is greater",b)
# else:
#     print("c is greater", c)


# larget of 4 



# check if number is a multiple of 7 or not 


# x = float(input("enter the number:"))

# if x % 7 == 0:
#     print("multiple of 7:",x)
# else:
#     print("not a multiple",x)


a=float(input("enter the number a:"))
b=float(input("enter the number b:"))
c=float(input("enter the number c:"))
d=float(input("enther the number d:"))

if a >= b and a >= c and a >= d:
    print("a is greater", a)
elif b >= c and b >= d and b >= a:
    print("b is greater",b)
elif c >= d and c >= a and c >= b:
    print("c is grater", c)
else:
    print("d is grater", d)
