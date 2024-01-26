# Calculator
first_number = int(input("Enter first number: "))
operator = input("Enter operator +,-,×,÷: ")
second_number = int(input("Enter second number: "))

if operator == '+':
    print(first_number + second_number)
    
elif operator == '-':
        print(first_number - second_number)
        
elif operator == '×':
    print(first_number * second_number)

elif operator == '÷':
        print(first_number / second_number)