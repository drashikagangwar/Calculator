# Mini Project: Real World Calculator

def calculator():
    print("\n==============================")
    print("       SMART CALCULATOR")
    print("==============================")

    while True:
        print("\nOperations: +  -  *  /")
        print("Type 'exit' to close the calculator.")

        first = input("\nEnter first number: ")

        if first.lower() == "exit":
            print("Calculator closed.")
            break

        try:
            num1 = float(first)
            operator = input("Enter operation: ")

            if operator not in ["+", "-", "*", "/"]:
                print("Invalid operation!")
                continue

            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2

            print(f"Result: {num1:g} {operator} {num2:g} = {result:g}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")


calculator()