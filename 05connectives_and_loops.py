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
