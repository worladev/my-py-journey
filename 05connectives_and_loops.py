'''
CONNECTIVES AND LOOPS

CONNECTIVES
Connectives are powerful tools in discrete mathematics that enable us
to build complex statements from simpler ones. These logical operators
have real-world applications and are indispensable in coding and
problem-solving. This study note aims to provide a comprehensive
understanding of connectives, their applications, and exercises to
reinforce the concepts for entry-level students.

Section 1
Key Connectives and Real-World Examples

Conjunction (AND)
Real-world Example: To go on a trip, both the train tickets should be
booked (P) and the weather forecast should be clear (Q).
Coding Application: In coding, "AND" is used to create compound conditions
that require both conditions to be true for an action to take place.

# P: both the train tickets should be booked
# Q: the weather forcast should be clear
'''
is_train_tix_booked = True
is_weather_clear = False

if is_train_tix_booked and is_weather_clear:
    print("You can go on a trip")
else:
    print("You cannot go on a trip")


'''
Real-world Example:
To go on a picnic, both the weather should be sunny (P) and the food should be ready (Q).
Coding Application: In coding, "AND" is used to create conditional statements where both
conditions must be true for an action to occur.

# P: the weather should be sunny
# Q: the food should be ready
'''
is_weather_sunny = False
is_food_ready = False
if is_weather_sunny and is_food_ready:
    print("You can go on a picnic!")
else:
    print("You cannot go on a picnic!.")

'''
Disjunction (OR):
Real-world Example: A student can choose to study either French (P) or Spanish (Q) as a foreign language.
Coding Application: "OR" in coding allows for multiple possibilities, and the code proceeds if at least one condition is true.

# P: student choose French
# Q student choose French
'''
is_french_student = False
is_spanish_student = False
if is_french_student or is_spanish_student:
    print("You are studying a foreign language!")
else:
    print("You are not studying a foreign language!.")

'''
Real-world Example: For an elective course, a student can choose to take either Chemistry or Physics (P)
and Math or English as a core course
Coding Application: In coding, "OR" allows programmers to provide multiple options or conditions,
and the code proceeds if at least one condition is true.

P: student choose Chemistry
Q: student choose Physics
R: student choode Math
S: student choose English

Note: It is important to break compound statement into smaller manageable statements
'''
is_chemistry_student = False
is_physics_student = True
is_math_student = True
is_english_student = False

if (is_chemistry_student or is_physics_student) and (is_math_student or is_english_student):
    print("Your course selection is complete")
else:
    print("Your course selection is incomplete!.")


'''
Negation (NOT):
Real-world Example: A restaurant sign reads: "We do NOT serve breakfast after 10:00 AM."
Coding Application: "NOT" is used to reverse the truth value of a condition. For example,
"IF NOT raining THEN go to the park."

P: we serve breakfast at 10pm
'''
is_10am_breakfast = True
if not is_10am_breakfast:
    print("Breakfast not served at 10am!")
else:
    print("Breakfast served at 10am!.")


'''
Section 2
Applying Connectives to Coding Questions

Scenario: Voting Eligibility Checker
Exercise:
Explanation: In this example, we use the "AND" connective to ensure both age and citizenship are
met before declaring a person eligible to vote.
'''
age = 18
citizen = True
if age >= 18 and citizen:
    print("You are eligible to vote!.")
else:
    print("You are not eligible to vote.")


'''
Scenario: Fruit Shopping
Explanation: Here, the "OR" connective allows the code to check if the fruit matches any of
the specified options to decide whether it is available for purchase.

'''
fruit = "apple"
budget = 20

if fruit == "apple" or fruit == "banana" or fruit == "orange":
    print("You can buy this fruit.")
else:
    print("This fruit is not available.")


'''
Scenario: Discount Calculation
Explanation: This code uses the "AND" connective to apply a 10% discount only if the customer
purchases three or more items with a total cost exceeding $100.
'''
items = 5
total_cost = 200
if items >= 3 and total_cost > 100:
    discount = total_cost * 0.1
    final_cost = total_cost - discount
else:
    final_cost = total_cost
print("Your final cost is: " + str(final_cost))

'''
Scenario: Age Group Classifier
Explanation: In this example, the "AND" connective is used to define the age range for adults
(between 18 and 64) as a logical condition.
'''
age = 30

if age < 18:
    group = "Child"
elif age >= 18 and age < 65:
    group = "Adult"
else:
    group = "Senior"
print("You belong to the ", group, "group.")


'''
Scenario: Weather Condition Checker
Explanation: Here, "OR" connective is used to check whether it's raining (weather == "rainy") or
if the person already has an umbrella (umbrella is True) before advising to take an umbrella.
'''
weather = "rainy"
unbrella = True

if weather == "rainy" or unbrella:
    print("Take an umbrella with you.")
else:
    print("The weather is clear, No need for and umbrella.")



'''
SECTION 3 (TASKS)
Logical Connectives in Decision Making

*** Your task is to use your understanding of connectives to solve the below problems.
Remember to make your submissions using colab ***

Scenario: Weekend Plans
Exercise:
Write a Python program that takes two inputs from the user:
"Is it Saturday?" (sat) and "Is it Sunday?" (sun). If either of these inputs is true, the program should
display "Let's have fun!" Otherwise, it should display "Weekdays are for work."

TASK 1
'''

sat = input("Is it Saturday? (enter yes/no): ")
if sat == 'yes':
    it_is_sat = True
else:
    it_is_sat = False

sun = input("Is it Sunday? (enter yes/no): ")
if sun == 'yes':
    it_is_sun = True
else:
    it_is_sun = False


if it_is_sat or it_is_sun:
    print("Let's have fun!")
else:
    print("Weekdays are for work.")


'''
TASK 2

Scenario: Ticket Purchase
Exercise:
Write a Python program that takes two inputs from the user:
"Is the customer a student?" (student) and "Is the customer a senior citizen?" (senior).
If the customer is a student OR a senior citizen, the program should display "You are eligible for a
discount!" Otherwise, it should display "No discount available."
'''
customer_type = input("Is the customer a student? (enter yes/no): ")
if customer_type == 'yes':
    is_a_student = True
else:
    is_a_student = False

customer_type2 = input("Is the customer a senior citizen? (enter yes/no): ")
if customer_type2 == 'yes':
    is_a_senior_citizen = True
else:
    is_a_senior_citizen = False


if is_a_student or is_a_senior_citizen:
    print("You are eligible for a discount!.")
else:
    print("No discount available.")


'''
TASK 3

Scenario: Password Verification
Exercise:
Write a Python program that asks the user to enter a password. If the password matches "Secret123,"
the program should display "Access granted." Otherwise, it should display "Access denied."
'''
correct_password = "Secret123"

passw = input("Enter your password: ")
if passw == correct_password:
    print("Access granted")
else:
    print("Access denied")


'''
TASK 4

Scenario: Temperature Classification
Exercise:
Write a Python program that takes the temperature as input. If the temperature is less than 0 degrees
Celsius OR greater than 30 degrees Celsius, the program should display "Extreme weather conditions.
Stay indoors." Otherwise, it should display "Enjoy the day!"
'''
temp = int(input("Enter temperature: "))
if temp < 0 or temp > 30:
    print("Exteme weather conditions. Stay indoors.")
else:
    print("Enjoy the da!")


'''
LOOPS
Understanding the Need for Loops in Coding

Loops are indispensable tools in programming that allow us to execute a set of instructions repeatedly.
This lecture introduces entry-level students to the concept of loops, discusses when and why loops are
needed in coding, and presents examples of common real-world scenarios where loops are essential.

1. Why Do We Need Loops?
Loops provide an efficient way to perform repetitive tasks in programming.They save time and effort by
automating tasks that would otherwise require manual repetition. Loops are used to process collections
of data, such as lists or arrays.

2. When Do We Use Loops?
Loops are ideal when dealing with iterative processes, such as iterating through a list of names, numbers,
or records. When performing calculations that require multiple iterations or successive changes to a
variable's value, loops become crucial. Loops are employed when working with data structures that require
traversal, searching, or filtering.

3. Real-World Examples of Loop Application
a) Calculating the Sum of Numbers:
Given a list of numbers, use a loop to calculate their sum and display the result.

b) Displaying Multiplication Table:
Create a loop that prints the multiplication table of a given number up to a specified limit.

c) Validating User Input:
Use a loop to repeatedly prompt the user for valid input until the correct data is provided.

Page 2: Basic Structure of Loops
Loop Structure
This section explores the basic structure of loops, focusing on entry-level loop constructs and the
concept of the terminating condition. Students will learn the fundamentals of "for" loops and
"while" loops, which are commonly used in coding.

1. For Loops
For loops are used when the number of iterations is known beforehand.

The basic structure of a for loop:
for variable in sequence:
	# Code block to be executed on each iteration

The loop iterates through each element in the sequence, and the specified code block is executed for
each iteration.

2. While Loops
While loops are used when the number of iterations is not known in advance, and the loop continues
until a specified condition becomes false.

The basic structure of a while loop:
while condition:
	# Code block to be executed on each iteration

The loop continues as long as the condition remains true, and it terminates once the condition becomes
false.



Examples and Practical Exercises
This page includes practical coding examples and exercises to solidify students' understanding of loops.
These exercises will apply the concepts learned and challenge students to create their own loop solutions.

1. Example: Sum of Numbers
Task: Calculate the sum of all numbers from 1 to a given positive integer.
'''
# Using for loop
num = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print("Sum of numbers from 1 to", num, "is: ", sum)

'''
2. Example: Displaying Multiplication Table
Task: Print the multiplication table of a given number up to a specified limit.
'''
# Using while loop
num = int(input("Enter the number for multiplication table: "))
limit = int(input("Enter the limit for the table: "))
i = 1
while i <= limit:
    result = num * i
    print(num, "x", i, "=", result)
    i += 1

'''
3. Exercise: Fibonacci Series
Task: Generate the Fibonacci series up to a given number.
'''
# Using for loop
n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


'''
4. Exercise: Guessing Game
Task: Implement a simple guessing game using a while loop where the user has to guess a secret number.
'''
import random
secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number (1-100): "))
    if guess < secret_number:
        print("Try again! The secret number is higher.")
    elif guess > secret_number:
        print("Try again! The secrete number is lower.")
    else:
        print("Congratulations! You guessed the secret number!")

'''
Loops are essential tools in programming, enabling us to solve repetitive tasks efficiently.
By understanding the concept of loops, the basic structure, and how to determine when to use them,
entry-level students can tackle a wide range of coding challenges and explore the endless possibilities
of programming. With practice and application, students will gain confidence in using loops to solve
complex problems and build valuable coding skills.
'''