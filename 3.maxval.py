# maximun no from 3 no

num1=int(input('Enter the num1:'))
num2=int(input('Enter the num2:'))
num3=int(input('Enter the num3:'))


if num1!=0 or num2!=0 or num3!=0:
    if (num1>num2 and num1>num3):
        print(f"{num1} is greater no..")
    elif(num2>num1 and num2>num3):
        print(f"{num2} is greater no..")
    else:
        print(f'{num3} is greater no..')
else:
    print("Please enter the valid no")