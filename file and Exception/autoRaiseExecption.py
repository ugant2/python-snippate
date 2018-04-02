import  traceback
def a():
    b()
def b():
    c()

def c():
    d()

def d():
    print(1 /0)

try:
    a()
except Exception:
    print("Error")
    traceback.print_ex()



