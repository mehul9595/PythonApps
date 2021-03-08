print("Welcome to Python Calculator!")
print("""
Select the operation you want to do
1. Addition
2. Subtraction
3. Multiply
4. Divide""")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x/y

def main():
    while True:
        choice = input("Enter your choice 1/2/3/4: ")
        
        if choice in ("1", "2", "3", "4"):
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        
            if choice == "1":
                print(add(x, y))
            elif choice == "2": 
                print(subtract(x, y))
            elif choice == "3":
                print(multiply(x, y))
            elif choice == "4":
                print(divide(x, y))
            
        else:
            print("Didn't select valid operation")

if __name__ == "__main__":
    main()
