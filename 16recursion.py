### Tower of Hanoi

# Recursive function for Tower of Hanoi
from hashlib import new


def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')



### String Reversal
    #str[start:stop:step]

trial = 'reversal'
new_trial = trial[::-1]
print(new_trial)


    #using recursion
def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:]) + str[0]

str = 'worlasi'
reverse = string_reversal(str)
print(reverse)