# # # list

# # marks=[1, 2, 3, 4, 5]

# # print(marks)

# # print(marks[2])

# # print(len(marks))

# # student=["dhruv", 45, 21, "surat"]

# # print(student)

# # student[2]=22

# # print(student)
# # # list are mutable 

# # # list has slicing 

# # print(student[1:3])

# mark=[55, 66, 33, 22, 56, 55]

# print(mark[1:])

# # it support negative index

# print(mark[-3:-1])

# mark.append(54)

# print(mark)

# # two type assending small to big 
# mark.sort()

# print(mark)

# # desending big to small 

# mark.sort( reverse=True )

# print(mark)

# # it reverse 

# mark.reverse()

# print(mark)

# # it add element in specific index

# mark.insert(2, 5)

# print(mark)

# # it remove list 

# mark.remove(33)

# print(mark)

# # pop rmeove specic index

# mark.pop(4)

# print(mark)

# ask user three input and stored as list 

# a=input("enter movie a:")
# b=input("enter movie b:")
# c=input("enter movie c:")

# list_movie= [a, b, c]

# x=type(list_movie)
# print(x)

# print(list_movie)



# check list is continer palindrome of elemnt 

list_pali=[1,2,3,2,1]

copy_list=list_pali.copy()

copy_list.reverse()

if list_pali == copy_list:
    print("value is palindrome")
else:
    print("value is not palindrome")


