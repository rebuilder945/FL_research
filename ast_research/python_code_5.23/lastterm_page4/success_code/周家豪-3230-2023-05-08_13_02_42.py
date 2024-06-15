lst=eval(input())
atr=''
lst.sort(reverse=True)
for x in lst:
    atr+=x
int(atr)
print(atr)
