import os 

# # # file read and close 
# # x=open("hello.txt", "a")
# # # # read all file
# # # data = x.read()
# # # print(data)

# # # print()
# # # # read only one line in file it empty output
# # # y= x.readline()
# # # print(y)

# # # this is read and delete old and write new thing 
# # x.write("\nhello this is raju")


# # x.close()

# # it will change data form starting 
# f = open("hello.txt", "r+")

# f.write("abc")

# f.close()

# # w+ it complete wipe out and start new file as read 

# # a+ append in the last read + append

# it automatically close file 
# with open("hello.txt", "r") as file:
#     x=file.read()
#     print(x)

# print()

# with open("hello.txt", "w") as file:
#     x=file.write("new data")

# os.remove("hello.txt")

# with open("practice.txt", "w") as f:
#     f.write("hi everyone\nwe are learning file i/o\n")
#     f.write("using py\nlike program in java")

# with open("practice.txt", "r") as f:
#     data = f.read()

#     if data.find("learning") != -1:
#         print("found")
#     else:
#         print("not found")

# new_data=data.replace("java", "py")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

def check_for_line():
    data = True
    line_no=1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if "learning" in data :
                print(line_no)
                return
            line_no+=1

    return -1


check_for_line()