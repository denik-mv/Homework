a = int(input('Enter a first number (a): '))
b = int(input('Enter a second number (b): '))
x = int(input('Enter a thirst number (x): '))
print('{} between {} and {} is {}'.format(x, min(a, b), max(a, b), a < x < b or a > x > b))