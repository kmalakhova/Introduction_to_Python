'''
Copeland’s Corporate Company also wants to update how they generate temporary passwords for new employees.

Write a function called password_generator that takes two inputs, 
first_name and last_name and then concatenate the last three letters of each and returns them as a string.

'''

first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name

new_account = account_generator(first_name, last_name)

print(new_account)