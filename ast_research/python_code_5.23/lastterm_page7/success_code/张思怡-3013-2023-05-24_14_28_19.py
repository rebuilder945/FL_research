m=1
dict={}
while m:
    a=input()
    if (a =='ok'):
        m=0
    else:
        k,v=a.split(" ")
        dict[k]=int(v)
    
# print(dict)
list1=list(dict.keys())
list2=list(dict.values())
list1.sort()
list2.sort()
print(list1)
print(list2)
print('yes'if 'India'in list1 else'no')
print(sum(list2))
