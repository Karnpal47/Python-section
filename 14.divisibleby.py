# 12)delete each element in the list which is divisible by 2 or all the even numbers.

list = [8,7,5,33,256,234,95,101]
for num in list:
    if num%2==0:
        list.remove(num)
print(list)
