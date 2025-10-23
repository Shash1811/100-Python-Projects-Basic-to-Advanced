import art
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
operations = {"+":add,
              "-":sub,
              "*":mul,
              "/":div}
def calculator():
    print(art.logo)
    sset = True
    num1 = float(input("Enter your first number:"))
    for symbol in operations:
        print(symbol)
    while sset:
        operator = input("Enter the operation to be performed:")
        num2 = float(input("Enter the next number:"))
        answer = operations[operator](num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")
        next = input("Type 'y' if you want to continue with the same number or else tupe 'n' for new values")
        if next == 'y':
            num1 = answer
        else:
            sset = False
            print("\n"*20)
            calculator()
calculator()
