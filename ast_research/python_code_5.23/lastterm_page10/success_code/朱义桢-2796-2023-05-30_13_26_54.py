a=input()
if a.isalpha():
    print("No digits")
else:
    b=[]
    for i in range(len(a)):
        for x in range(i+1,len(a)):
            if a[i:x+1].isdigit():
                b.append(a[i:x+1])
    b.sort(key=len,reverse=True)
    m=[]
    for x in b:
        if len(x)==len(b[0]):
            m.append(x)
    m.sort()
    print(m[-1])
