

fib = [0,1,1,2,3,4,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print(list(result))


result1 = filter(lambda a: a, fib)
print(list(result1))
# result1 = filter([1], fib)
# print(list(result1))