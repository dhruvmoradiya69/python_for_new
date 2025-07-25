# # same as list but not change value 

# tup=(2,3,42,21,33,221)

# print(tup)

# print(tup[2])

# tup2=(2,)

# print(type(tup2))


# # slicing

# print(tup[1:3])

# print(tup.index(42))

# print(tup.count(21))


list_of_grade=["c","d","a","a","b","b","a"]

conv_tupe=tuple(list_of_grade)

print(conv_tupe.count("a"))

print(conv_tupe)

list_of_grade.sort()

print(list_of_grade)