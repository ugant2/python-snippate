f_col = []
s_col = []
t_col = []

matrix = [[1,2,3], [4,5,6], [7,8,9], [4,9,2]]

for row in matrix:
    f_col.append(row[0])
    s_col.append(row[1])
    t_col.append(row[2])

print(f_col)
print(s_col)
print(t_col)

print("\n")

#printing countries and their city
#use of nested loop

countries = [["nepal", ["surkhet", "nepalgunj"]], ["china", ["beijing", "sanghai"]], ["india", ["banglore", "lacknow"]]]

for con in countries:
    print("countreis:")
    print(con[0])
    for city in con[1]:
        print("city:")
        print(city)

print("\n")

numbers = [["even", [2,4,6]], ["odd", [3,5,7]]]
for even in numbers:
    print(even[0])
    for odd in even[1]:
        print(odd)