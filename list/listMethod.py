#append() method
t = ["a", "f", "h", "p", "c", "l"]
t.append("z")
print(t)

print("\t")

#extend() method
a = [3, 5, 6, 8]
b = [123, 567]
a.extend(b)
print(a)

print("\t")

#sort() method are void. they modify list and return none
s = ["r", "f", "a", "o", "c", "z"]
s.sort()
print(s)

print("\t")
#sum() built in function to sum

s = [1,2,3,5]
sum(s)  #sum() is also called REDUCE cause it cmbines a siquence into a single value
print(s)


print("\t")

def add_all(t):
    total = 0
    for x in t:
        total += x #argumented assingment
    return total #total is a accumulator; it accumulate sum of the element

print("\t")

("Write a function called nested_sum that takes a nested list of integers and add up\n"
 "the elements from all of the nested lists.")

L = [1,3,4,5]
def nested_sum(L):
    total = 0
    for i in L:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
        return total
