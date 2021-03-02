# Attempt to derive random digits from time.time() 
# First uploaded on 2021-3-2 # (MIT license) 
# Kenneth Burchfiel

import time
import math
import matplotlib.pyplot as plt

# The goal of this program is to convert a current timestamp into a digit
# between 0 and 9 that is at least somewhat random.

def get_digit():
    current_time = time.time()
    ct_decimal_component, ct_seconds_component = math.modf(current_time)
    # Splits the current time into its decimal component and its seconds
    # component (the latter of which is not used in the program) Because the
    # decimal component of current_time extends for many digits, I figured that
    # the digits 8+ places to the right should be quite random (as it would be
    # hard for a human to time the program to output a desired number).
    # print(current_time) print(ct_decimal_component)
    decimal_to_int = ct_decimal_component*10000000
    # print(decimal_to_int)
    potentially_somewhat_random_digit = int(decimal_to_int % 10) # Uses
    # the modulus operator to return the ones digit of decimal_to_int
    # print(potentially_somewhat_random_digit)
    return potentially_somewhat_random_digit

# Part 1 of the program: a while loop that allows a user to print multiple
# 'random' numbers

while(True):
    entry = input("Press Enter to retrieve a semi-random digit \
    between 0 and 9, or Q plus Enter to quit.")
    if entry.lower() == 'q':
        break 
    print("Your digit is",get_digit())

# Part two of the program allows the user to test how random the program's
# output is. The user is asked to press 'enter' 100 times to produce 100
# 'random' numbers, after which a histogram will be generated using the list of
# those random numbers.

digit_list = []
for i in range (100):
    input("Press Enter to add a new digit to the list.")
    if i % 1000 == 0:
        print("now on interation #",i)
    digit_list.append(get_digit())

print(digit_list)
plt.hist(digit_list, bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.xticks(ticks=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5],
labels=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) # Offsetting 
# the tick locations by 0.5 to the right allows for the labels to appear
# directly under the tick marks, which is ideal for this type of histogram.
plt.show()
    

