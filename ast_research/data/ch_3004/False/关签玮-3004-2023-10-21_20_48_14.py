lst=eval(input())
for i in lst:
    for q in range(2,i,1):
        if i%q==0 or i==1:
            lst.remove(i)
            break
print(lst)
