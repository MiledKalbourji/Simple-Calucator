def calculator(): 
    while True:
        # Print options for the user 
        print("Enter '+' to add two numbers") 
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 'quit' to exit")

        # Get user input
        user_input = input(": ")

        # Check if the user wants to quit
        if user_input == "quit":
            break

        # Check if the user input is a valid operator
        elif user_input in ["+", "-", "*", "/"]:
            # Get the first number
            num1 = float(input("Enter a number: "))

            # Get the second number
            num2 = float(input("Enter another number: "))

            # Perform the operation based on the user input
            if user_input == "+":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")

            elif user_input == "-":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")

            elif user_input == "*":
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")

            elif user_input == "/":
                # Handle division by zero
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
        else:
            # In case of invalid input
            print("Invalid input, please try again.")


# Call the calculator function to start the program 
calculator()
