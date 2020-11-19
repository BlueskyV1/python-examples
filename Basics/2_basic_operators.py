# 1. Operators
# ================
num1 = 1.5
num2 = 6.3

# Add two numbers
sum = 0
# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Subtract two numbers
sub = 0
# Display the sum
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, sub))

# Store input numbers
num3 = input('Enter first number: ')
num4 = input('Enter second number: ')

# Modulus of two numbers
mod = 0
# Display the sum
print('The modulus of {0} and {1} is {2}'.format(num3, num4, mod))

num = 8
# Calculate the square root
num_sqrt = 0
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

# 2. Find the area of triangle
# ============================
a = input('Enter first side: ')
b = input('Enter second side: ')
c = input('Enter third side: ')

# calculate the semi-perimeter : s = (a+b+c)/2
s = 0
# calculate the area : area = √(s(s-a)*(s-b)*(s-c))
area = 0

print('The area of the triangle is %0.2f' %area)

# 3. Swap two variables
# ============================
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# method 1: create a temporary variable and swap the values
temp = 0

# method 2: swap the values without using temporary variable

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
