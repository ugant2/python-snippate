# # g = lambda name: lambda age: name + str(age)
# # nFunc = g("ram")(50)
# # print(nFunc)
# #
# # print("\n")
# #
# # g = lambda age: "adult" if age > 18 and age < 50 \
# #     else ("child" if age < 18 and age > 5 else "baby")
# #
# # print(g(3))
#
# print("\n")
#
# g = lambda age: "teen" if age > 10 and age < 18 else ("adult" if age > 18 and age < 40 else("old" if age > 40 else "child"))
#
# print(g(48))
#
# print("\n")
#
# g = lambda name#parameter, age#parameter: "teen" + str(age) if age > 10 and age < 18\
#     else ("adult" + str(age) if age > 18 and age < 40\
#     else("old" + str(age) if age > 40 else "child" + str(age)))
# print(g("ram", 5))

# def check(name,age):
#     if age > 10 and age < 18:
#         print(name + str(age))
#     elif age> 18 and age < 40:
#         print("adult")
#     elif age>40:
#         print("old")
#     else :
#         print("child")
#
# check("hjfh",12)
#
#
# print("\n")

# def farhenit(T):
#     return ((float(9)/5)* T + 32)
# def celcius(T):
#     return((float(5)/9)* T-32)
# temp  = (36.5, 37,37.5, 39)
# F = map(farhenit, temp)
# print(list(F))
# C = map(celcius, F)
# print(list(C))
#
# #map(function, value)
# G = map(lambda  T: (float(9)/5)* T + 32,temp)
# H = map(lambda  T: (float(5)/9)* (T - 32),F)
# print(list(G))

temp  = [36.5, 37,37.5, 39]
a = [(float(9)/5)* i + 32 for i in temp]
print(a)

