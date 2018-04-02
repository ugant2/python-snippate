#for loop

for i in [1,2,3,4]:
    print(i)


for i in "Hello":
    print(i)

print('\n')

for i in [[1,2,3], [4,5,6]]:  #nested loop
    for j in i:
        print(j)

print('\n')

countries = [["Nepal", ["ktm", "pkr"]],["India", ["Delhi","Mumb"]],["USA", ["DC", "NYC"]]]
for i in countries:
    print('countries')
    print(i[0])
    print("cities:")
    for j in i[1]:
        print(j)


print("\n")

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# i=0
# for m in matrix:
#     for j in m:
#         i +=1
#         print(m[i])

matrix = [[1,2,3], [4,5,6], [7,8,9]]

f_col = []
s_col = []
t_col = []

for row in matrix:
    f_col.append(row[0])
    s_col.append(row[1])
    t_col.append(row[2])

print(f_col)
print(s_col)
print(t_col)

print("\n")


#continue statement

for item in [1,2,3,4,5]:
    if item == 3:
        continue
    print(item)


print("\n")
#break statment

for item in [1,2,3]:
    for letter in "hello":
        if letter == "e":
            break
        print(letter)
    print(item)


print("\n")

countries = {"Nepal": ["ktm", "pkr"],"India": ["Delhi","Mumb"],"USA": ["DC", "NYC"]}

for k, v in countries.items():
    print(k)
    print(v)

