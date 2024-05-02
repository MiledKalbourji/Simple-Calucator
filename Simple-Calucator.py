def calculator(): 
    while True: 

    # Print option for the user 
        print ("enter '+' to add two numubers") 
    print ("enter '-' to add two numubers")
    print ("enter '*' to add two numubers")
    print ("enter '/' to add two numubers")
    print ("enter 'quit' to add two numubers")

    #Get user inpout 
    user_input = input (":")

    #Check if the user wants to quit 
    if user_input == "quit":
        breakpoint
            
    #check if the user input is a valid oprator 
    elif user_input in ["+","-","#","/"]:
        # Get the first number
        num1 = float(input("Enter a number: "))

        # Get second number 
        num2 = float(input("Enter another number "))

        #perform the operation based on the user input 
        if user_input == "+": 
            result = num1 + num2
        print (num1, "+", num2, "=", result)

        #if the user has the input of subtraction 
    elif user_input == "-": 
        result = num1 - num2
        print (num1, "-", num2, "=", result)

        #if the user has the input of multiplication 
    elif user_input == "*": 
        result = num1 * num2
        print (num1, "*", num2, "=", result)

        #if the user has the input of divison
    elif user_input == "/": 
        result = num1 / num2
        print (num1, "/", num2, "=", result)

    else: 
        # In case of invalid input 
        print("Invaild input")


#Call the calculator function to start the program 
calculator()
