number = int(input("Enter a number to see its multiplication table:"))

for i in range(1,11):
    multiplication = number * i
    print(f"{number}*{i}={multiplication}")
    i +=1