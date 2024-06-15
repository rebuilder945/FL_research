sText=input()
n=input()
if n not in sText:
    print(sText)
else:
    sNew=sText.replace(n,"",count=-1)
    print(sNew)
