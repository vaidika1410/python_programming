def sum(a,b):
    c = a + b
    global z
    z = 0
    return c

z = 8
print(z)
print(sum(2, 5))
print(z)