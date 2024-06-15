n=eval(input())
a=[]
b=''
if n>1 and n%1==0:
    for i in range(2,n+1):
        if i==int(str(i)[::-1]):
            a.append(i)
    list1 = a
    list2 = sorted(list1)
    for x in list1:
        if x == 1 or x == 0:
            list2.remove(x)
        else:
            for i in range(2,int(x/2)+1):
                if not x%i and x > 2 and x in list2:
                    list2.remove(x)
    for x in list2:
        b=b+str(x)+" "
    print(b[0:-1])
else:
    print('illegal input')
