'''Q. W A P which takes two numbers from the user and prints below output:-
1. num1 is greater than num2 if num1 is greater than num2
2. num1 is smaller than num2 if num1 is smaller than num2
 3. num1 is equal to num2 if num1 and num2 are equal'''

# if-else

x = int(input("Enter the first number: "))
y = int(input("Enter the first number: "))

# if x>y:
#     print('{} is greater than {}'.format(x,y))
# elif x<y:
#     print('{} is smaller than {}'.format(x,y))
# elif x==y:
#     print('{} and {} are equal'.format(x,y))

# ternary operator

print('{} is greater than {}'.format(x, y) if x > y else ('{} is smaller than {}'.format(x, y)) if x < y else (
    '{} and {} are equal'.format(x, y)))
