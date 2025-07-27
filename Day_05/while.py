# # count=1

# # while count <= 5:
# #     print("hwllo")
# #     count+=1


# # i=1

# # while i <= 5:
# #     print(i)
# #     i+=1 # i = i + 1


# # o=5

# # while o >= 1:
# #     print(o)
# #     o-=1


# i = 1

# while i <= 100:
#     print(i)
#     i+=1

# print()

# x=100

# while x >= 1:
#     print(x)
#     x-=1

# print()

# n= int(input("enther the number:"))
# y=1

# while y <= 10:
#     print(n*y)
#     y+=1 


nums = [1,4,9,16,25,36,49,64,81,100]
i=0

while i < len(nums):
    print(nums[i])
    i+=1


num = (1,4,9,16,25,36,49,64,81,100)

i=0
x=49

while i < len(num):
    if num[i] == x:
        print("found", i)
        break
    else:
        print("find..")
    i+=1

# break and continue

a=0

while a <=5:
    if a==3:
        a += 1
        continue
    print(a)
    a+=1



# 