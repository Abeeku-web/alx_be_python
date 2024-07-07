["num1, num2, operation"]

def perform_operation(num1,num2,operation):

    if operation == "add":
        sum = num1 + num2
        print(sum)
    elif operation == "subtract":
        difference = num1 - num2
        print(difference)
    elif operation == "multiply":
        product = num1 * num2
        print(product)
    elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            division = num1/num2
            print(division)
    else:
        print("Invalid opertion entered, please try again.")


    
    
#     match operation:
#         case "add":
#             sum = num1 + num2
#             print(sum)
#         case "subtract":
#             difference = num1 - num2
#             print(difference)
#         case "multiply":
#             product = num1 * num2
#             print(product)
#         case "divide":
#             try:
#                 division = num1/num2
#                 print(division)
#             except ZeroDivisionError:
#                 print("Cannot divide by zero")
# perform_operation(10,5,"divide")


 