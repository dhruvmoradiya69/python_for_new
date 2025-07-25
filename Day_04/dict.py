# info = {
#     "name":"dhruv",
#     "age": 30,
#     "is_happend": True,
#     "list_store": [ 50, 40, 60],
#     "tuple_store": ( 50, 44, 33 )
# }

# # dictionary store all type of data 
# print(info)


# # access value from dict
# print(info["name"])

# # change name 

# info["name"] = "raju"

# # add new value
# info["surnamr"] = "rastogi"

# print(info)


# # empty dict
# empty = {}

# print(empty)

# # dict in dict like nested dict
# print()

# student={
#     "name": "dhruv",
#     "subj": {
#         "phy": 34,
#         "che": 33,
#         "math": 32
#     }
# }

# # print netsed dictionary data 
# print(student["subj"]["phy"])


# # methods

# # return all keys

# print(student.keys())

# # return all key values

# print(student.values())

# # return all key avlue pair as tupele

# print(student.items())

# # returns all the key value

# print(student.get("name"))

# # update add new dict key value pair pass

# student.update({"city" : "surat"})

# print(student)

# coll_dict = {
#     "table": ["a piece of furniture","list of facts & figures"],
#     "cat": "a small animal"
# }

# print(coll_dict)


marks = {}

sub=str(input("enter the subject:"))
mark=float(input("enter the marks:"))

marks.update({ sub : mark })

print(marks)