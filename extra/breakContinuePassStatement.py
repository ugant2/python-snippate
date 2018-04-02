#break statement
print("this is BREAK statement")
for letter in "Python":
    if letter == "h":
        break
    print("current letter: ", letter)


print("\n")

var = 10
while var > 0:
    print("current variable value :", var)
    var = var - 1
    if var == 6:
        break
print("goodbye!")


#continue statment
print("ths is CONTINUE statement")
for letter in "python":
    if letter == "h":
        continue
    print("current letter: ", letter)

print("\n")

var = 10
while var > 0:
    var = var - 1
    if var== 5:
        continue
    print("current variable value: ", var)

print("\n")

print("this is PASS statement")

for letter in "python":
    if letter == "h":
        pass
        print("this is pass block")
    print("current letter: ", letter)