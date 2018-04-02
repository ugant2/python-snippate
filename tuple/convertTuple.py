#string formating
val1 = "integer"
val2 = 2
print("the %s value is equal to %d." %(val1, val2))

print("\n")

tuple1 = (1,2,3,4) #packing a tuple
print(tuple)

print("\n")

first, second, third, fourth = tuple
print(first)
print(second)
print(third)
print(fourth)

print("\n")

#in-place variable swapping
bug = "weevil"
bird = "African swallow"

bug, bird = bird, bug
print(bug)
print(bird)

print("\n")

#converting lists and tuples
my_list = ["run", "jump", "attack"]
my_tuple = ("hammer", "shotgun", "knuckle")

print(tuple(my_list)) #convert list into tuple
print(list(my_tuple)) #convert tuple into list