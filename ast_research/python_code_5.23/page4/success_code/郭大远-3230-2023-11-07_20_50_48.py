list1=list(input())
list2=[]
for i in range(len(list1)):
    a=(eval(list1[i])+5)%10
    list2.append(a)
list2.reverse()
h=int(''.join(map(str,list2)))
print(h)
