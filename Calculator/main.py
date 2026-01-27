#Calculator
try:
    solution = input("Simple calculator. Select the operating mode: \n" \
    "1 - Insert each character separately \n" \
    "2 - Paste the entire expression at once \n")
    if solution == "1":
        while True:
            try:
                num1, num2, operand = input("Insert first number: "), input("Insert second number: "), input("Operand sign: ")
                expression = eval(num1 + operand + num2)
                print(f"Result: {expression}")
            except Exception: print("Not correct numbers or operand!")
    elif solution == "2":
        while True:
            try:
                final_expression = ""
                expression = input("Insert the complete expression: ")
                for symbol in expression:
                    if symbol != " ":
                        final_expression = final_expression + symbol
                print(f"Result: {eval(final_expression)}")
            except Exception: print("Unexpected error")
    else:
        print("Incorrect parameter")
except KeyboardInterrupt: print("\nThe calculator has finished working")