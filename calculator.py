num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
operator=input("enter the operation you want to perform (+,-,*,/)")
if operator =="+":
    print( num1 + num2)
elif operator == "-":
    print (num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2!=0 :
        print( num1 / num2)
    else :
        print("cannot divide by 0")
else :
    print(" invalid operator")
    
