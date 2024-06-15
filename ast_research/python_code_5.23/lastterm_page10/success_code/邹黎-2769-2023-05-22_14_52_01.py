a=input()
lst1=("abcdefghijklmnopqrstuvwxyz")
lst2=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
str=""
for x in a:
    if x=="a":
        str+="z"
    if x=="A":
        str+="A"
    
    elif (x in lst1):
            str+=lst1[26-lst1.find(x)-1]
    elif (x in lst2):
            str+=lst2[26-lst2.find(x)-1]
    else:
        str+=x
print(str)
print(a)
