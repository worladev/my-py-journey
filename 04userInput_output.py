### Get input from users typed through the keyboard and display them to the console.
user_details = {}

print("Accepting the following user details to \n update records in the system.")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
email = input("Type your email address here: ")

print("\n")
print("User Details")
print("Firstname: ", first_name)
print("Surname: ", last_name)
print("Age: ", age)
print("Email: ", email)

# Performing some basic calculations with user inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add_num = num1 + num2
print("Adding the two numbers = ", add_num)

sub_num = num1 - num2
print("Subtracting second number from first number: ", sub_num)

mul_num = num1 * num2
print("Multiplying the numbers: ", mul_num)

div_num =  num1 / num2
print("Dividing first number by second number: ", div_num)