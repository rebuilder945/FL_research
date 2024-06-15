a=input()
list1=[]
longest=[]
for i in range(len(a)):
    if "0"<=a[i]<="9":
        list1.append(a[i])
        if len(list1)>=len(longest):
            longest=list1.copy()
    else:
        list1=[]
if len(longest)>0:
    print("".join(longest))
else:
    print("No digits")
