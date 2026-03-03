# check if a string is palindrome

string = "abccba"

if string == string[::-1]:
    print('palindrome')
else:
    print('not a palindrome')