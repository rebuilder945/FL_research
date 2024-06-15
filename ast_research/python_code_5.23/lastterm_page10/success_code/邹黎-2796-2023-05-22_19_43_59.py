a=input()
c=0
lst=[]
max=1
lst1=[]

for x in a:
    if x in list("1234567890"):
        c+=1
if c==0:
    print("No digits")
else:
    for x in range(0,len(a)):
        if a[x] in list("1234567890"):
            lst.append(x)
    for x in lst:
            geshu=1
            
            str=a[x]
            while True:
                if (x+1) in lst:
                    geshu+=1
                    x+=1
                    str+=a[x]
                else:
                    break
            lst1.append(str)
            if geshu>=max:
        
                max=geshu
    for x in reversed(lst1):
        if len(x)==max:
                print(x)
                break
        
