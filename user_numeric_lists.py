"""
Desiree Thomopson
January 26, 2023
My domain is dogs

Pratice working with list by working through the examples below. 
"""

# import some modules first - how many can you make use of?

import math
import numbers
import statistics
import random


# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = length * width  # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

# generate random list of numbers
# list = [random.randint(1, 20) for i in range(15)]

# created list1 using the randomly generated list
list1 = [
    62,
    65,
    87,
    19,
    55,
    185,
    144,
    74,
    23,
    101,
    180,
    173,
    27,
    65,
    97,
    21,
    131,
    157,
    94,
    89,
    141,
    139,
    194,
    50,
    93,
    117,
    70,
    87,
    61,
    83,
    114,
    122,
    98,
    111,
    102,
    162,
    29,
    24,
    66,
    126,
    46,
    52,
    114,
    131,
    27,
    116,
    190,
    5,
    48,
    93,
]

listx = [94, 109, 143, 69, 167, 69, 186, 136, 54, 21]
listy = [1, 5, 4, 7, 9, 13, 20, 45, 50, 70]

# Descriptive: Averages and measures of central tendency
mean = statistics.mean(list1)
median = statistics.median(list1)
mode = statistics.mode(list1)

# Descriptive: Measures of spread

stdev = statistics.stdev(list1)
variance = statistics.variance(list1)

# Descriptive: Measures of correlation
correlationxy = statistics.correlation(listx, listy)

# Predictive: Machine Learning - Linear Regression
slope, intercept = statistics.linear_regression(listx, listy)

# Predict the y value for a given x value
newx = 15

# Use the slope and intercept to predict a y value for the future x value
newy = slope * newx + intercept

min = min(list1)
max = max(list1)
len = len(list1)
sum = sum(list1)
average = sum / len
set1 = set(list1)
sorted = sorted(list1)
list1.sort(reverse=True)  # ssorted()  # Using Reverse = True

# Created a "new short list" for section Lists 4. List Method
lst = [20, 18, 16, 20, 14, 13, 3, 19, 20, 15, 17, 19, 2, 16, 15]

copied_lst1 = lst.copy()
copied_lst1.append(43)

copied_lst2 = lst.copy()
copied_lst2.extend((9, 11, 13, 16))

copied_lst3 = copied_lst2.copy()
copied_lst3.insert(10, 56)

copied_lst4 = copied_lst3.copy()

if 5 in copied_lst4:
    copied_lst4.remove(5)
    copied_lst4.append(31)
else:
    copied_lst4 = 'There are no changes as 5 was not in the prior list'
    
copied_lst5 = copied_lst3.copy()
copied_lst5.count(2)                     

copied_lst6 = copied_lst5.copy()
copied_lst6.sort()

copied_lst7 = copied_lst6.copy()
copied_lst7.sort(reverse=True)                     

copied_list8 = copied_lst7.copy()

copied_lst9 = copied_lst7.copy()
copied_lst9.pop()

copied_lst10 = copied_lst9.copy()
copied_lst10.pop(-1)

# Lists 5 Using Filter() and Map()
def is_even(x):
    return x % 2 == 0
filter_copied_lst10 = list(filter(is_even, copied_lst10))

map_copied_lst10 = list(map(lambda x: x ** (1/3), copied_lst10))

vol_copied_lst10 = list(map(lambda x: x * x * x, copied_lst10))

#Lists 6. List Transformations - Using List Comprehension

less_copied_lst1 = [x for x in list1 if x < 50]

cubed_copied_lst1 = [x ** 3 for x in list1]

div_copied_lst1 = [x / 2.5 for x in list1]
    


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    # print("your code here")

    # print(get_area_of_lot(4, 6))
    # print(list)
    print("Task 3. Numeric List")
    print("Lists:")
    print(f"list1:\n {list1}.")
    print()
    print(f"listx:\n {listx}.")
    print()
    print(f"listy:\n {listy}.")
    print()
    print("**********List 1: List Statistics**********")
    print(
        f"1. The mean, median and mode of list1 are {mean:.02f},{median:.02f} and {mode:.02f} respectively."
    )
    print(
        f"2. The standard deviation and variance of list1 is {stdev:.02f} and {variance:.02f} respectively."
    )
    print()
    print("**********List 2: Lists - Correlation and Prediction**********")
    print(f"1. The correlationxy of listx and listy is {correlationxy:.02f}")
    print(
        f"2. The slope and intercept of listx and listy are {slope:.02f} and {intercept:.02f}"
    )
    print("3. x has been set to 15 for a future time")
    print(
        f"4. When setting the future value for x to {newx}, the new y value is equal to {newy:.02f}"
    )
    print()
    print("**********Lists 3. Lists - Using Python Built-in Functions**********")
    print(f"1. The min of list1 is {min}.")
    print(f"2. The max of list1 is {max}.")
    print(f"3. The length of list1 is {len}.")
    print(f"4. The sum of list1 is {sum}.")
    print(f"5. The average of list1 is {average:.02f}.")
    print()
    print(f"6. The following is a set which has been created from list1:\n{set1}.")
    print()
    print(f"7. The following is list1 after it has been sorted:\n{sorted}.")
    print()
    print(
        f"8. The following is list1 after the list has been sorted in reverse order:\n{list1}."
    )
    print()

    print("**********Lists 4. List Methods**********")
    print(f"Randomly generated a new short list:\n{lst}.")
    print()
    print(f"1. Appended the single value of 43 to the list:\n{copied_lst1}.")
    print()
    print(f"2. Extended the list with 9, 11, 13 and 16:\n{copied_lst2}.")
    print()
    print(f"3. Inserted the number 56 at index 10:\n{copied_lst3}.")
    print()
    print(f"4. The updated list:\n{copied_lst4}.")
    print()
    print(f"5. The number 2 appears in the list {copied_lst5.count(2)} time.")
    print()
    print(
        f"6. Sorted the list using .sort() to reflect ascending order:\n{copied_lst6}"
    )
    print()
    print(
        f"7. Sorted the list using .sort(reverse=True) to reflect descending order:\n{copied_lst7}"
    )
    print()
    print(f"8. Copied the list using .copy():\n{copied_list8}")
    print()
    print(
        f"9. Utilized pop() to remove the first item off the top of the list /stack:\n{copied_lst9}"
    )
    print()
    print(
        f"10. Utilized pop() to remove the last time off the bottom of the list/stack:\n{copied_lst10}"
    )
    print()
    print("**********Lists 5. List Transformations - Using filter() and map()**********")
    print(f'1. Used filter() to filter to only the even numbers in the list:\n{filter_copied_lst10}.')
    print()
    print(f'2. Used map() to map each x to the cuberoot of x in the list:\n{map_copied_lst10}.')
    print()
    print(f'3. Used map() to map calculate the volume of a cube with a side equal to the value in the list:\n{vol_copied_lst10}.')
    print()
    print('**********List 6. List Transformations - Using List Comprehension**********')
    print(f'1. Used a list comprehension to filter x for each x in list1 that is less than 50:\n{less_copied_lst1}.')
    print()
    print(f'2. Used a list comprehension to triple each value in list1:\n{cubed_copied_lst1}.')
    print()
    print(f'3. Used a list comprehension to divide each value in list1 by 2.5:{div_copied_lst1}.')
    


# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.
