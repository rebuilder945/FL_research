a=str(input())
list1=[]
for x in a:
    b=(int(x)+5)%10
    list1.append(b)
list1.reverse()
s=''
for x in list1:
    s+=str(x)
print(int(s))
