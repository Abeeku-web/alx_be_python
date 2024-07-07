def perform_operation(num1,num2,operation=None):
    
    match operation:
        case "add":
            sum = num1 + num2
            print(sum)
        case "subtract":
            difference = num1 - num2
            print(difference)
        case "multiply":
            product = num1 * num2
            print(product)
        case "divide":
            try:
                division = num1/num2
                print(division)
            except ZeroDivisionError:
                print("Cannot divide by zero")
perform_operation(10,0,"divide")

 