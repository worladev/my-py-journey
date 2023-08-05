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

