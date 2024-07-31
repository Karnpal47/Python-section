#count the number of occurrences of x in the given list.

l=['a','h','l','x','c','x','f','x','h','a','x']
lt=[]
for i in l:
    if(i=='x'):
        lt.append(i)
print(len(lt))
