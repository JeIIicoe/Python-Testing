# Testing conditional statements
import json

a=1
b=2

print('\nConditional Tests:')
print('\nVariable a is' , 'One' if (a == 1) else 'Not one')
print('Variable a is', 'Even' if (a % 2 == 0) else 'Odd' , '\n')

# Writing Lists

months = ['January', 'Febuary', 'March', 'April']
coords = [[1, 2, 3], [4, 5, 6]]

print('List Tests:\n')
print('First Month:', months[0])
print('Second Month:', months[1])
print('Third Month:', months[2])

print('\nTop Left:', coords[0][0])
print('Bottom Right:', coords[1][2])

print('\nSecond Month First Letter:', months[1][0])