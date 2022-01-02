def product (first, second):
    if second == 0:
        return  "second value is 0" 
    elif first == 0:
        return " value is 0"
    elif second == 1:
        return first
    elif first == 1:
        return second
    else:
        return str(first) + ' + ' + str(product(first, second - 1 ))

first_number = input('please enter first number: ')
while not first_number.isdigit():
    first_number = input('Use digits only: ')
second_number = input('please enter second number: ')
while not second_number.isdigit():
    second_number = input('Use digits only: ')


X = int(first_number)
Y = int(second_number)
print()
print(product(X,Y), '=', X, '*', Y, '=', X*Y )