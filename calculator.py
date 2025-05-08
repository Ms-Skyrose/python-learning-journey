def add(num1, num2):
    ans = num1 + num2
    print(f"Addition of {num1} and {num2} is {ans}")

def subtract(num1, num2):
    ans = num1 - num2
    print(f"Substraction of {num1} and {num2} is {ans}")
   
def multiply(num1, num2):
    ans = num1 * num2
    print(f"Multiplication of {num1} and {num2} is {ans}")

def divide(num1, num2):
    if num1 or num2 != 0:
        ans = num1 / num2
        print(f"Division of {num1} and {num2} is {ans}")
    else:
        print("Please this is undefied due to zero")



def main():
    while True:
        print("This is a calculator for your sum, subtraction, multiplication and division operations")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Exit")

        choice = int(input("Choose an option"))
        if choice in (1,2,3,4):
            num1 = float(input("Enter a number"))
            num2 = float(input("Enter a number"))
            if choice == 1:
                add(num1, num2)
            elif choice ==2:
                subtract(num1, num2)
            elif choice == 3:
                multiply(num1, num2)
            elif choice == 4:
                divide(num1, num2)
            else:
                print("Please enter a valid number from the options provided")
            
            print()
            input("Press Enter to continue.....")

        elif choice == 5:
            print("Successfully exited")
            break
        
        
if __name__ == "__main__":
    main()