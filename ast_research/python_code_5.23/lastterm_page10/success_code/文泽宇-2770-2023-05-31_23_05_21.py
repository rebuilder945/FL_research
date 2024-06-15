n=input()
m=input()
lst1=[i for i in n]
lst2=[j for j in m]
lst1.sort()
lst2.sort()
c=0
if len(lst1)!=len(lst2):
    print('False')
else:
    for i in range(0,len(lst1)):
        if lst1[i]==lst2[i]:
            c+=1
    if c == len(lst1):
        print('True')
        
