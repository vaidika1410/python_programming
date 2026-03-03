# string slicing methods

name = 'vaidikakaul1410'

print(name[0:])
print(name[0:-1])
print(name[2:-1])

# slicing with skipping characters
print(name[0:10:1]) #skips 0 character
print(name[0:10:2]) #skips 1 character

# incomplete argument range
print(name[0:]) # till last index
print(name[:15]) # from first index