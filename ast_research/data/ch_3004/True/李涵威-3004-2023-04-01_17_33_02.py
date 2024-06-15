lst=eval(input())
for i in lst[:]:
    if i<=1:
        lst.remove(i)
    if i>=2 and type(i)==int:
        for x in range(2,i//2+1):
            if i%x==0:
                lst.remove(i)
                break
print(lst)
