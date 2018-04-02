# Create a dictionary to store your academic details. It should contain information about
# you and your courses. Try to demonstrate the use of data structures(tuples, lists and
# dictionaries) we learned in first class. Include as many operations as you can. It is up to
# you​ ​ to​ ​ decide​ ​ on​ ​ data​ ​ organization​ ​ and​ ​ operations.

details = {"name":"ugant", "age":21, "course":["adi", "nsc", "dw", "isa"]}
details["phone"] = [983464]
print(details, "\n") # add key and value in the dictionery

print(details.items(), "\n") #gives in the form of key and value

del details["age"] #delete key and value
print(details, "\n")

l = [k for k in details] #prints key only from dictionery, using list comprehension
print(l, "\n")

print(details.values(), "\n") #print all the values from the dictionery

#using exception in the program
try:
    p = lambda age: age in details
    print(list(p), "\n")
except ValueError:
    print("enetr correct type of the value")
finally:
    print("exception not found")


