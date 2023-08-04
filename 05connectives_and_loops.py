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

