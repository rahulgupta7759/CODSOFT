num1=float(input("enter first number  :"))
num2=float(input("enter second number :"))
  
print("1.addition")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=int(input("choose any operation.for choosing simply press number 1,2,3 or 4  :"))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif  choice == 4:
    print(num1/num2)
else:
    print("invalid input")        
