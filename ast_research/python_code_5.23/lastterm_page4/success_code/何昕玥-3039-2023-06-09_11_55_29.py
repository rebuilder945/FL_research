lst=eval(input())
sMax=max(lst)
sMin=min(lst)
for i in lst:
    if i==sMax or i==sMin:
        lst.remove(i)
print(lst)

