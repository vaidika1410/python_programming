# lambda functions are anonymous functions and used when writing compact code

square = lambda a: a*a

'''
similar to writing
def square(a):
    return a*a
'''

print(square(2))

sum = lambda a, b: a+b

print(sum(4, 6))