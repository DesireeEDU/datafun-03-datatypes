"""
Desiree Thompson
January 31, 2023
My domain is dogs

Pratice working with string list by working through the examples below.

"""

# imports first
import random
import math
import numbers
import statistics

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

dog_names = ['Cynthia', 'Hailey', 'Halo', 'Shiloh', 'Saige', 'Emmie', 'Layne', 'Lucy', 'Clyde', 'Caiden', 'Kora', 'Jake']

dog_breeds = ['Akita', 'Hound', 'Shepherd', 'Beagle', 'Dalmation', 'Terrier', 'Chihuahua', 'Bulldog', 'Retriever', 'Poodle', 'Pug', 'Greyhound']

dog_colors = ['black', 'brown', 'golden', 'gray', 'white', 'brindle', 'mulitcolor']

dog_supplies = ['food','bowl','collar', 'leash', 'toy', 'brush', 'bed', 'treat']

dog_commands = ['sit', 'down', 'roll', 'paw', 'crate', 'up', 'walk', 'stay', 'wait', 'come', 'no', 'heel', 'speak', 'quiet']

length = len(dog_names)
new_set = set(dog_supplies)

# String Lists 2. Random Choice
sentence = (f'{random.choice(dog_names)} the dog is a {random.choice(dog_colors)} {random.choice(dog_breeds)} that loves their {random.choice(dog_supplies)} and only follows the {random.choice(dog_commands)} command.')

# String Lists 3. Get Unique Words
with open("text_woodchuck.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()
    unique_words = set(list_words)
    
sorted_list = sorted(unique_words)

# Printed Information
print('Task 4. String Lists')
print('String Lists')
print()
print(f'1. List of dog names:\n{dog_names}.')
print()
print(f'2. List of dog breeds:\n{dog_breeds}.')
print()
print(f'3. List of dog colors:\n{dog_colors}.')
print()
print(f'4. List of dog supplies:\n{dog_supplies}.')
print()
print(f'5. List of dog commands:\n{dog_commands}.')
print()
print()
print('String Lists 1. Using Python Built-In Functions')
print(f'1. The number of names within the dog names list is {len(dog_names)}.')
print()
print(f'2. The supplies list is converted into a set as shown below. The set is identical to the list except with curly brackets and a different presentation order:\n   {set(dog_supplies)}.')
print()
print(f'3. Using the built-in zip function I was able to combine two lists into tuples as shown below:')
for name, breed in zip(dog_names, dog_breeds):
    print(f'   {name} is a(n) {breed}.')
print()
print()
print(f'String Lists 2. Random Choice')
print(f'1. A random supply from the supplies list is a {random.choice(dog_supplies)}.')
print()
print('2. The following uses the sentence generator to develop random sentences about the domain. ')
print(sentence)
print()
print()
print('String Lists 3. Get Unique Words')
print(f'1. A list of unique words from the Woodchuck text includes:\n {unique_words}')
print()
print(f'2. When the list is sorted, it appears as follows:\n{sorted_list}')
print()
print(f'3. The sorted list has {len(sorted_list)} items included.')



    