def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/": divide,
}
def calculator():
    print("Welcome to the Python Terminal Calculator!")
    num1 = float(input("What's the first number? "))
    for item in operations:
        print(item)
    operation_symbol = input("Pick an operation from the lines above: ")
    if operation_symbol not in operations:
        print("That is not a valid symbol. Please restart program.")
        return
    num2 = float(input("What's the second number? "))

    for item in operations:
        if item == operation_symbol:
            math = operations[operation_symbol]
            answer = math(num1, num2)
            break
        elif operation_symbol not in operations:
            print("That is not a valid symbol. Please restart program.")
            break

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_variable = 1
    while continue_variable == 1:
        continue_question = input("""Would you like to continue by doing
        further calculations from your answer? 
        Please type 'y' for yes and 'n' for no. """).lower()
        if continue_question == "n":
            continue_variable -= 1
            break
        for item in operations:
            print(item)
        operation_symbol = input("Pick an operation from the lines above: ")
        if operation_symbol not in operations:
            print("That is not a valid symbol. Please restart program.")
        num2 = float(input("What's the next number? "))
        for item in operations:
            if item == operation_symbol:
                math = operations[operation_symbol]
                new_num1 = answer
                new_answer = math(new_num1, num2)
                break
            elif operation_symbol not in operations:
                print("That is not a valid symbol. Please restart program.")
                break
        answer = new_answer
        print(f"{new_num1} {operation_symbol} {num2} = {answer}")
    calculator()
calculator()