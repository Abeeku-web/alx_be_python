def perform_operation(num1,num2,operation):
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    operation = input("Choose the operation(+,-,*,/):")
    match operation:
        case "+":
            sum = num1 + num2
            print("The result is {sum}.")
        case "-":
            difference = num1 - num2
            print("The result is {difference}.")
        case "*":
            product = num1 * num2
            print("The result is {product}.")
        case "/":
            try:
                division = num1/num2
                print("The result is {division}.")
            except ZeroDivisionError:
                print("Cannot divide by zero")
 