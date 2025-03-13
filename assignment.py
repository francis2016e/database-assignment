num1 = int(input('input number: '))
num2 = int(input('input number: '))
operation = input('enter the operation (-,+,/,*): ')

if operation == '-':
     result = num1 - num2
elif operation == '+':
     result = num1 + num2
elif operation == '/':
     result = num1 / num2
elif operation == '*':
     result = num1 * num2

print(f'{num1} {operation} {num2} = {result}')


