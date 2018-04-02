f=''
try:
    f = open("/home/ugantx/Downloads/abc.txt","r")
    print(f.read())
except IOError:
    print("file not found")
finally:
    print("closed")
    f.close()
