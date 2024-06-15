lst=eval(input())
lst2=[]
key=0
for i in lst:
    if i==0:
        lst2.append(i)
        key+=1
for i in range(key):
    lst.remove(0)
    print(lst+lst2)
