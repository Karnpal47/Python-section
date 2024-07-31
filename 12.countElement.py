# 10) write a Python program to count Even and Odd numbers in a List.

l=[2,3,5,6,54,34,87,43,11,23,23,234,232,123,654,555]
even_count=0
odd_count=0
for i in l:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print('Even no in list=',even_count)
print('Odd no in list=',odd_count)

