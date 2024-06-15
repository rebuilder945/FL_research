lst=eval(input())
atr=''
lst.sort(reverse=True)
for x in lst:
    atr+=str(x)
print(int(atr))
