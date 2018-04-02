# pythonic way to check if something exists? [duplicate]

#trick 1
from extra.breakContinuePassStatement import var

print("LBYL style, 'look before you leap'")
var_exists = 'var' in locals() or 'var' in globals()

#trick 2

print("EAFP style, 'easier to ask forgiveness than permission'")
try:
    var
except NameError:
        var_exists = False
else:
    var_exists  = True