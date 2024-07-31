#The task is to print all words with even length in the given string.”This is a python Language”.

str='This is a pyt language'
str1=str.split()
l=[]
for i in str1:
    if len(i)%2==0:
        l.append(i)
print(l)        
