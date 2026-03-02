# strings are immutable --> meaning that the original string cannot be changed
# if a string is modified, it is stored as a completely new variable, keeping the original string intact

name = "vaidika kaul"

print(name)
print("uppercase name: ", name.upper())
print("lowercase name: ", name.lower())
print("capitalized name: ", name.capitalize())

print("name: ", name)
print(len(name))


# strip methods --> removing whitespaces
string = "    vaidika    "
print('strip: ', string.strip())
print('Lstrip: ', string.lstrip())
print('Rstrip: ', string.rstrip())

# find and replace method
text = "python is fun"
print(text.find('is')) # finds and returns the index of first occurence
print(text.replace('fun', 'awesome')) # replaces all the occurences and returns a new string

# split method
fruits = "Apples, Bananas, Strawberries"
print(fruits.split(',')) # splits the string on the basis of ',' and returns a list

print(",".join(['Apples', ' Bananas', ' Strawberries']))

# string test
word = 'abc123'
print(word.isalpha()) # checks if the string contains all alphabets
print(word.isnumeric()) # checks if the string contains all numericals
print(word.isalnum()) # checks if the string contains alphabets and numerical values
print(word.isspace()) # checks if the string contains spaces 