# # string data type store a sequence of characters

# # \n create or say print in new line
# str1="hello with \n dhh"
# # \t create space between value
# str2='dhruv moradiya \t hello'

# print(str1)
# print(str2)
# # escap sequence charachert 

# # ope 1 concatenation

# a="hello"
# b="world"

# print(a + " " + b)

# # ope 2 lenth calculate all number

# c="hello i am devops"
# print(len(c))

# # indexing in string measn character got one placed num
# # it start with 0 

# index_ste="i am dhruv with devops and cloud"

# char= index_ste[5]

# print(char)
   
# # slicing it will part of sting start and end give output

# sli_str="this is slicing"

# # sli_str[5:len(sli_str)]
# # if you forgat any start or last index python automatic understand

# print(sli_str[2:7]) # output: is is 

# # negative index

# min_str="this is min sli"

# print(min_str[-3:-1])


# # string function inbuild

# str_in="this is devops script"

# print(str_in.endswith("pt")) # give true and false check and comaper end string 

# # capitalize

# print(str_in.capitalize()) # give first charater on capital in only one time 

# print(str_in.replace("is", "are")) # replace form number and charachter

# print(str_in.find("devops")) # it find word give starting index 

# print(str_in.count("is")) # it cound totla characheter give on number

# print(str_in.upper())



# prac 1 user input and print it lenth

x=input("enter the string:")

print(len(x))


# find one charater how many time come


y="enter the string with come $ and not $ also with come in $ bro you $  is hign"

print(y.count("$"))
