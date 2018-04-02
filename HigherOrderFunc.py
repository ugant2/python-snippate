def odd(n):
    return n%2==1

def test(a):
    return a(4)

print(test(odd))