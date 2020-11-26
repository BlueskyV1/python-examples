# iterator module

import operator
import time

# Defining lists
L1 = [1, 2, 3]
L2 = [2, 3, 4]

# Starting time before map
# function
t1 = time.time()

# Calculating result
a, b, c = map(operator.mul, L1, L2)

# Ending time after map
# function
t2 = time.time()

# Time taken by map function
print("Result:", a, b, c)
print("Time taken by map function: %.6f" % (t2 - t1))

# Starting time before naive
# method
t1 = time.time()

# Calculating result usinf for loop
print("Result:", end=" ")
for i in range(3):
    print(L1[i] * L2[i], end=" ")

# Ending time after naive
# method
t2 = time.time()
print("\nTime taken by for loop: %.6f" % (t2 - t1))

# infinite iterators

import itertools

# for in loop
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")

count = 0

# for in loop
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1

l = ['Geeks', 'for', 'Geeks']

# defining iterator
iterators = itertools.cycle(l)

# for in loop
for i in range(6):
    # Using next function
    print(next(iterators), end=" ")

# using repeat() to repeatedly print number
print ("Printing the numbers repeatedly : ")
print (list(itertools.repeat(25, 4)))

# import the product function from itertools module
from itertools import product

print("The cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print()

print("The cartesian product of the containers:")
print(list(product(['geeks', 'for', 'geeks'], '2')))
print()

print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))

# import the product function from itertools module
from itertools import permutations

print("All the permutations of the given list is:")
print(list(permutations([1, 'geeks'], 2)))
print()

#Terminating iterators
print("All the permutations of the given string is:")
print(list(permutations('AB')))
print()

print("All the permutations of the given container is:")
print(list(permutations(range(3), 2)))

# import combinations from itertools module
from itertools import combinations

print("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(['A', 2], 2)))
print()

print("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2)))
print()

print("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(range(2), 1)))

# import combinations from itertools module

from itertools import combinations_with_replacement

print("All the combination of string in sorted order(with replacement) is:")
print(list(combinations_with_replacement("AB", 2)))
print()

print("All the combination of list in sorted order(with replacement) is:")
print(list(combinations_with_replacement([1, 2], 2)))
print()

print("All the combination of container in sorted order(with replacement) is:")
print(list(combinations_with_replacement(range(2), 1)))

# accumulate()
import itertools
import operator

# initializing list 1
li1 = [1, 4, 5, 7]

# using accumulate()
# prints the successive summation of elements
print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))

# using accumulate()
# prints the successive summation of elements
print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))

