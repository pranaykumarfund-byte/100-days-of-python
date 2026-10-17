age = int(input("Enter your Age:"))
print("Your age is:",age)
print(age<=18)
print(age>=18)
print(age == 18)
print(age!=18)
if(age>=18):
    print("you can Drive")
else:
    print("You cannot Drive")
applePrice = int(input("ENter you apple price:"))
budget = 200
if(budget-applePrice>50):
    print("Alexa, add 1 kg apples to the cart.")
elif(budget-applePrice >70):
    print("Alexa,you can buy")
else:
    print("Alexa,do not buy apple")
num = int(input("enter you number:"))
if(num<0):
    print("number is negitive")
elif(num == 0):
    print("number is zero")
elif(num == 0):
    print("number is 0")
else:
    print("number is positive")
print("iam happy")
num = int(input("enetr your number"))
if(num<0):
    print("number is negitive")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num<=20):
        print("numbr is between 10-20")
    else:
        print("number is greater than 20")
else:
    print("numbr is zero")
    