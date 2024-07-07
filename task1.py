number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
operator=input("Enter operator: ")
if operator=="+":
   print(number1+number2)
elif operator=="_":
   print(number1-number2)
elif operator=="*":
   print(number1*number2)
elif operator=="%":
   print(number1%number2)
elif operator=="/":
   print(number1/number2)  
else :
   print("Invalid operator, can't be calculated")
