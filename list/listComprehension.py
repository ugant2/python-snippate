# a = (1,2,3,4,5,6,7,8,9,10,20,30,33)
#
# even = []
#
# for i in a :
#     if i%2 == 0:
#         even.append(i)
#
#
#
# # same program using list comprehension
#
# even_new = [i for i in a if i%2==0]
#
# print(even)
# print(even_new)
#
#
# #nested list comprehension
# even_new = [i for j in a for i in j if i%2==0]

name = [["ram", 18], ["shyam", 20], ["hari", 23]]
l = [age for tup in name for age in tup if (type(age) == int and age > 18)] #age is a paramater to be printed

print(l)