size = int(input("Enter the size of the pattern:"))

current_row = 0

while current_row < size:
    for i in range(1,size+1):
        print("*",end="")
    print()
    current_row += 1