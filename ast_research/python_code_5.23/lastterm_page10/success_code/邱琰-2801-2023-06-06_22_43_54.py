n=input()
tem=[]
longest=[]
for i in n:
    if '0'<=i<='9':
        tem.append(i)
        if len(tem)>=len(longest):
            longest=tem
    else:
        tem=[]
if len(longest)>0:
    print(''.join(longest))
else:
    print('No digits')
