lst=eval(input())
atr=''
lst.sort(reverse=True)
for x in lst:
    atr+=str(x)
int(atr)
print(atr)
