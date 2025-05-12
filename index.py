def main():
    # Get input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform calculation based on operation
    if operation == "+":
        result = num1 + num2
        operator_name = "addition"
    elif operation == "-":
        result = num1 - num2
        operator_name = "subtraction"
    elif operation == "*":
        result = num1 * num2
        operator_name = "multiplication"
    elif operation == "/":
        # Check for division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operator_name = "division"
    else:
        print("Invalid operation. Please use +, -, *, or /")
        return
    
    # Display the result
    print(f"{num1} {operation} {num2} = {result}")
    print(f"The result of {operator_name} is {result}")

if __name__ == "__main__":
    main()