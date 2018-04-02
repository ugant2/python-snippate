numbers = [1,4,5,3]

for i in range(len(numbers)):
     numbers[i] = numbers[i] * 2
print(numbers)


print("\t")


 # empty list is never executed
for x in []:
     print("this never happen")

print("\t")

# nested list
a = ['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print(a)
print(len(a))

print("\t")
#concatenate list
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

print("\t")

#astrik(*) repaets the list
repeat = [1,2,3,4] * 3
print(repeat)

print("\t")

t = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(t[1:3])
print(t[3:])
print(t[:])

#sice list is mutable it can be changes or updated
t[1:4] = ["x", "y"] #ask in the class later
print(t)


print("\t")


