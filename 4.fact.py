num=int(input('Enter the num:'))
fact=1
if num>0:
    for i in range(1,num+1):
        fact=fact*i
    print(f"Factorial of {num} is:",fact)
else:
    print("Enter the positive no:")