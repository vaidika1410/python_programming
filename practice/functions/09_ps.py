# write a function that has a local variable which is incremented each time the function is called

def increment():
    counter = 0
    return counter+1

print(increment())
print(increment())
print(increment())
print(increment())