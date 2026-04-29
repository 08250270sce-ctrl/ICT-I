print()
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print()
while True:
    print("SIMPLE CALCULATOR")
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    if y==0:
        print("Division by zero is undefined. Please enter a non-zero number and try again.")
        continue
    print()
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice = input("Enter choice(1/2/3/4/5): ")
    print()
    if choice == "1":
        print(x," + ", y," = ",add(x,y))
    elif choice == "2":
        print(x," - ", y," = ",subtract(x,y))
    elif choice == "3":
        print(x," x ", y," = ",multiply(x,y))
    elif choice == "4":
        print(f"{x} / {y} = {divide(x,y):.2f}")
    elif choice == "5":
        print("Exiting the calculator. GOODBYE!")
        break
    else:
        print("No operations are chosen.")
        break
    print()
print()