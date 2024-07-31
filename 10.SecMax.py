# 8)find the second largest number in the given list.

l=[2,0,-2,-7,2,3,5,6,54,34,87,43,11,23,23,234,232,123,654,555]
for i in l:
    l.sort()
print(l[1])