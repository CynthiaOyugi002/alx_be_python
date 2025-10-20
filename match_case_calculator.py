number1 = float(input("enter the first number:"))
number2 = float(input("enter the second number:"))
operation = input("choose the operation(+, -, *, /):")
match operation:
  case "+":
      result = number1 + number2
      print(f"the result is{result}")
  case "-":
      result = number1 - number2
      print(f"the result is{result}")
  case "*":
       result = number1 * number2
       print(f"the result is{result}")
  case "/":
      if number2 == 0:
          print("cannot divided by zero")
      else :
          result = number1 / number2
          print(f"the result is{result}")
  case _:
    print("invalid operation selected")