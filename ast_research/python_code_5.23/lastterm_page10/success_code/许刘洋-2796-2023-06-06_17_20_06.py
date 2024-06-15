a=input()
b=[]
longest=[]
for i in a:
    if i.isdigit():
        b.append(i)
        if len(b)>len(longest):
            longest=b.copy()
    else:b=[]
if longest==[]:
    print('No digits')
print(longest)

