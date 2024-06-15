lst=eval(input())
lst2=[]
for k in range(len(lst)):
    for i in lst:
        if i == max(lst):
            lst2.append(i*10**(len(lst)-1))
            lst.remove(i)
print(sum(lst2))
