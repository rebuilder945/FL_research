n=list(input())
lst1=[]
lst2=[]
for i in n:
    if '0' <= i <= '9':
        lst1.append(i)
        if len(lst1)>=len(lst2):
            lst2=lst1.copy()
    else:
        lst1=[]
if len(lst2)>=1:
    print(''.join(lst2))
else:
    print('No digits')
