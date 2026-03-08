# function that returns result of a/b, but returns a message if b is 0

def safe_divide(a, b):
    if b == 0: return 'cannot divide by zero'
    return a/b

print(safe_divide(6, 2))
print(safe_divide(4, 0))