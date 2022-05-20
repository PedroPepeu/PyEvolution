print("Calculator opened!!\n")
# confirmation = input("You want to add a number? (Y/N) ")   #more than 2 operators
print("WARNING! When you use non decimal numbers, do NOT use comma(,) only dot(.)\n\n")

number1 = float(input("Put your first number: \n"))
number2 = float(input("Put your second number: \n"))

print("Yout numbers are {:n} and {:n}".format(number1, number2))

operator = input("Which one you will use?\n + \n - \n * \n / \n ** \n") # add the rest in divided: added

if operator == "+":
  plus = number1 + number2
  print("Your answer is {:n}".format(plus))

elif operator == "-":
  minus = number1 - number2
  print("Your answer is {:n}".format(minus))

elif operator == "*":
  times = number1 * number2
  print("Your answer is {:n}".format(times))

elif operator == "/":
  divided = number1 / number2
  rest = number1 % number2 #right here, it will divide and show the rest, if it exist
  print("Your answer is {:n}".format(divided))
  if rest > 0:
    print("And the rest is {:n}".format(rest))

elif operator == "**":
  #if number1 < 0:
    #abs.number1
  #if number2 < 0:
    #abs.number2
  #print("Your value are now positive")
  pot = number1 ** number2
  print("Your answer is {:n}".format(pot))

else:
  print("Put a correct logical operator")
