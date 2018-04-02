
# option 1
n = [1,2,3,4,5,6,7,8,9,10]
m = [0,1,2,3,4,5,6,7,8,9,10]

result = [i*j for i in m for j in n ]
# print(result)

#option 2
table = [str([i*j for i in range(0,11)]) for j in range(1,11) ]
print(table)

