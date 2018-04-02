


import sys

try:
    f = open("myfile.ttt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS Error: {0}".format(err))
except ValueError:
    print("could not convert data to integer")
except:
    print("unexpected errors:", sys.exc_info()[0])
