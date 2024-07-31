#13)Remove empty List from List

list=[34,54,23,[],5,4,8,7,[],98]
Org_list=[]
for ele in list:
    if ele!=[]:
        Org_list.append(ele)
print("Original list after removing the empty lists=",Org_list)
