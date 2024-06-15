sText=input()
n=len(sText)
m=0
def isnotture(x):
    if x.isdigit():
        return False
    else: 
        return True

while m<n:
    if isnotture(sText[m])==True:
        sNew=sText.replace(sText[m]," ")
        sText=sNew
    m+=1
ls=list(map(int,sText.split()))
if ls==[]:
    print("No digits")
else:
    print(max(ls))


