# 11)write a Python program to count positive and negative numbers in a List.

l=[2,0,-2,-7,2,3,5,6,54,34,87,43,11,23,-23,234,232,-123,-654,555]
positive_count=0
negative_count=0
for num in l:
    if num!=0:
        if num>0:
            positive_count+=1
        else:
            negative_count+=1
print('The positive no in list l=',positive_count)
print('The negative no in list l=',negative_count)

