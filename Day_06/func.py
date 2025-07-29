# # function sefinations
# def calculate(a, b): # parameters
#     return a+b

# sum=calculate(5, 6) # functions call(argument)
# print(sum)

# def hello():
#     print("hello")

# hello()

# def avg(a,b,c):
#     avgrage=(a+b+c)/3
#     print(avgrage)

# avg(2,3,4)

# we can return or just print output

# def cal_prod(a=1,b=1):
#     print(a+b)
#     return a+b

# cal_prod()

# defalt give as last 

# cities = ["delhi", "surat", "pune"]

# # def print_len(s):
# #     print(len(s))


# # print_len(cities)


# def single_line(s):
#     for i in s:
#         print(i, end= " ")

# single_line(cities)

# n=5

# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact*=i
#     print(fact)
    
# factorial(5)


# def convert(usd_val):
#     inr_val= usd_val * 83
#     print(inr_val)

# convert(100)


# # numebr input odd sting odd and even string even

# def odd_even(num):
#     if num%2 == 0:
#         print("even")
#     elif num%2 != 0:
#         print("odd")
#     else:
#         print("invalid")


# x = int(input("enther the number:"))
# odd_even(x)

# recursion

# def show(n):
#     if n == 0: # base case 
#         return
#     print(n)
#     show(n-1)

# show(5)


# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return fact(n-1) * n


# print(fact(10))



# 

def resur(n):
    if n == 0:
        return 0
    return resur(n-1) + n

x = resur(10)
print(x)