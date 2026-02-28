age = 34 # integer
name = "Vaidika" # string
cgpa = 8.5 # float
is_completed = True
marks = [82, 91, 84, 95, 83] # list -> ordered, mutable collections
roll_no = [82, 91, 84, 95, 83] # tuple -> ordered, immutable collections
price = {99, 94.99, 29.99} # set -> unordered collections of unique elements
student = {
    "name" : name,
    "age" : age
}

# python is a dynamically typed langauge -> a programming language which does not need specifying types of variables

print(age)
print(type(age))

print(name)
print(type(name))

print(cgpa)
print(type(cgpa))

print(is_completed)
print(type(is_completed))

print(marks)
print(type(marks))

print(roll_no)
print(type(roll_no))

print(price)
print(type(price))

print(student)
print(type(student))