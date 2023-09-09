'''
BINARY SEARCH
'''
def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:

        # mid = (low + high) // 2  # not correct - could cause integer overflow
        mid = low + (high - low) / 2 # proper way
        mid_value = list[mid]

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            return mid # value found!
        
    return -1 # value not found


list = [4, 7, 8, 12, 45, 99, 102]

print(binary_search(list, 8))


'''
QUESTION:

You are tasked with creating a simple number guessing game. In this game, the computer generates a random number between a
specified range, and the player's goal is to guess that number as quickly as possible. To make the game more efficient, you
will implement it using a binary search algorithm.


Implement a Python function guess_the_number(lower, upper) that takes the following arguments:
lower: The lower bound of the range (inclusive) within which the random number will be generated.
upper: The upper bound of the range (inclusive) within which the random number will be generated.

'''

import random

def guess_the_number(lower, upper):

  # modify this so that range of random number generated is (upper-lower)
  random_number = random.randint()

  low = lower
  high = upper

  while(low <= high):
    mid = low + (high - low)//2

    if(mid == random_number):
       return mid # value found
    elif mid < random_number:
      low = mid + 1
    else:
       high = mid - 1
  
  return -1 # value not found

## Using binary search to find the square root of any number.
# -- Why is the code in this kind of loop i.e using while True
# -- Why is mid a float and not an integer
# -- Why are low and high updated to mid and not mid-1/mid+1  
def squareRoot(number):
   low = 0
   high = number
   
   accuracy = 0.0001 # You can make this a parameter to specify the accuracy.
   
   while True:
      mid = float(low + ((high - low) / 2))
      squared = mid * mid
      
      if squared - number <= accuracy:
         return mid
      elif squared < number:
         low = mid
      else:
         high = mid
      
      return mid
  