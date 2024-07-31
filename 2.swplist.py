#1)write a Python program to swap first and last element of the list

l=['banana','apple','grapes','kiwi']
a=l.index('banana')
b=l.index('kiwi')
l[a],l[b]=l[b],l[a]
print(l)