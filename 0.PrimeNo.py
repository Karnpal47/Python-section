# WAP to determine whether num is prime or not

num=int(input('Enter the number:'))
count=0
if num==1:
    print(f"{num} is not a prime number.")
for i in range(1,num+1):
    if(num%i==0):
        count+=1    
if count==2:
    print(f"The {num} is a prime number.")
else:
    print(f"The {num} is not a prime number.")