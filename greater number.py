num1=int(input("Enter the number1:- "))
num2=int(input("Enter the number2:- "))
num3=int(input("Enter the number3:- "))
if((num1>num2) and (num1>num3)):
    print("The num1 is greater:-",num1)
elif(num2>num3) and (num2>num1):
    print("The num2 is greater:-",num2)
else:
    print("The num3 is greater:-",num3)
