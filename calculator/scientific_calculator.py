import math

print (" + for addition")
print("- for subtraction")
print("/ for division")
print(" * for multiplication")
print(" ^ for power")
print("r for root")
print('% for modulus')
print("pie  for Pie")
print("e  for E")
print("sin  for sin(trig)")
print("cos  for cos(trig)")
print("tan  for tan(trig)")
print("!    for factorial ")
print(" ln   for ln (natural log)")

firstNumber = float(input("Enter first Number:"))
op = input("Enter the Operation:").lower()
secondNumber = float(input("Enter Second Number:"))

if op == "+":
    print (firstNumber, "+", secondNumber, "=", firstNumber + secondNumber )
elif op == "-": 
    print (firstNumber, "-", secondNumber, "=", firstNumber - secondNumber )
elif op == "*":
    print (firstNumber, "*", secondNumber, "=", firstNumber * secondNumber )
elif op == "/":
    print (firstNumber, "/", secondNumber, "=", firstNumber / secondNumber )
elif op == "^":
    print (firstNumber, "^", secondNumber, "=", firstNumber ** secondNumber )
elif op == "r":
    print (firstNumber, "root", secondNumber, "=", secondNumber ** (1 / firstNumber) )
elif op == "%":
    print (firstNumber, "%", secondNumber, "=", firstNumber % secondNumber )
#factorial
elif op == "!":
    theNumber = firstNumber = secondNumber 
    secondNumber = 1
    while firstNumber > 1:
        secondNumber *= firstNumber 
        firstNumber = firstNumber - 1  
    print ("n!(", theNumber, ")=", secondNumber )
elif op == "sin":
    print ("sin(", secondNumber, ")=", math.sin(secondNumber ))
elif op == "cos":
    print ("cos(", secondNumber, ")=", math.cos
    (secondNumber ))
elif op == "tan":
    print ("tan(", secondNumber, ")=", math.tan(secondNumber ))
elif op == "pie" or op == "pi":
    print ("Pie =", math.pi)
elif op == "e":
    print = ("E =", math.e)
elif op == "ln":
    print ("ln(", secondNumber , ")= ", math.log(secondNumber))
else:
    print ("incorrect operator") 