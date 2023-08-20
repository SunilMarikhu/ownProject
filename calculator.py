#Define operators:

operators = {"+": lambda x,y : x+y,
             "-": lambda x,y : x-y,
             "*": lambda x,y : x*y,
             "/": lambda x,y : x/y}

#Enter the numbers:

num1 = input("Enter the first number: ")
opertator = input("Enter the operator: ")
num2 = input("Enter the second number: ")

result = operators[opertator](num1, num2)
print(result)

main() #call the main function