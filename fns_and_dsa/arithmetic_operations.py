def perform_operation(num1,num2,operation):
    
    match operation:
        case "add":
            sum = num1 + num2
            print("The result is {sum}.")
        case "subtract":
            difference = num1 - num2
            print("The result is {difference}.")
        case "multiply":
            product = num1 * num2
            print("The result is {product}.")
        case "divide":
            try:
                division = num1/num2
                print("The result is {division}.")
            except ZeroDivisionError:
                print("Cannot divide by zero")
 