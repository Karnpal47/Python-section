
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
if x!=0 and y!=0:
    print('Before swapping\n','x=',x,'y=',y)
    temp=x
    x=y
    y=temp
print('After swapping\n','x=',x,'y=',y)

