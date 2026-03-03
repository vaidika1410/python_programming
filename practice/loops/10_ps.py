# ask the user to enter the correct password until they enter the correct one

correct_password = 'v14g10'
password = input("enter password: ")


while (password != correct_password):
    password = input("Wrong! Enter correct password: ")

print("Success! Logged in")

# while True:
#     password = input("enter password: ")
#     if(password == correct_password):
#         print('you entered correct password!!')
#         break
#     else:
#         print('password did not match')
