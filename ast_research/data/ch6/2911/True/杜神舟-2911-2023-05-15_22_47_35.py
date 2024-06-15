aa=input()
list1=[]
for x in aa:
    b=(int(x)+5)%10
    list1.append(b)
list1.reverse()
print(''.join(str(x) for x in list1))
