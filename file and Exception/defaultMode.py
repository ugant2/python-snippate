
# read(r) is the default mode
try:
    file = open("myfile")
    print(file.read())
    file.close()
except:
    print()

