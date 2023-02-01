"""
Desiree Thompson
January 31, 2023
My domain is dogs

Practice using the following examples for tuples, sets, and dictionaries.

"""

#Created Tuples

tupleA = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
tupleB = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)

#tuple concatenation
tupleCat = tupleA + tupleB

#tuple repetition
tupleTwice = tupleA * 5

#tuple member testing 
tupleD = (2, 4, 6)
hasOne = 1 in tupleD
hasFour = 4 in tupleD

#tuple indexing
my_tuple = (8, 9, 10)
first = my_tuple[0]
second = my_tuple[1]
third = my_tuple[2]
last = my_tuple[-1]

#Use tuples to return multiple values from a function

def division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = division(10, 5)

print()
print('Tuple Examples')
print(f'1. The following concatenates tuples A and B:\n   {tupleCat}.')
print(f'2. The following multiplies tupleA by 2:\n   {tupleTwice}.')
print(f'3. It is {hasOne} that tupleD includes the number 1.')
print(f'4. It is {hasFour} that tupleD includes the number 4.')
print(f'5. When the dividend is 10 and the divisor is 5 the quotient will be {q} with a remainder of {r}.')


#Created Sets
setA = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
setB = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}

#set union
setC= setA | setB

#set intersection
setD = setA & setB

#set difference
setE = setA - setB

#converting a set to a list
dog_names = ['Cynthia', 'Hailey', 'Halo', 'Shiloh', 'Saige', 'Emmie', 'Layne', 'Lucy', 'Clyde', 'Caiden', 'Kora', 'Jake','Saige', 'Emmie', 'Layne', 'Lucy']
new_set = set(dog_names)
no_dup_list = list(new_set)
no_dup_list = [new_set]



print()
print('Set Examples')
print(f'1. The following is a union of setA and setB:\n   {setC}')
print(f'2. The following reflects the intersection of setA and setB:\n   {setD}.')
print(f'3. The difference between setA and setB is:\n   {setE}.')
print(f'4. The following reflects the list of dog names with duplicates:\n   {dog_names}.')
print(f'5. The following reflects the the list after it has been converted to a set:\n   {new_set}.')



# dictionaries
with open('dog_data.txt') as file_object:
    word_list = file_object.read().split()
    
    word_counts = {word: word_list.count(word) for word in word_list}
       
print()
print('Dictionaries')
print(f'1. The following is included in the dog_data word list:\n   {word_list}.')
print(f'2. The following is reflects the count of words on the dog_data word list:\n   {word_counts}.')

#word_counts_dict = {word: dog_data.count(word) for word in dog_data}


