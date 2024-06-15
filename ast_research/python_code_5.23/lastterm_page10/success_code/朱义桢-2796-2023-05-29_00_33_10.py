a=input()
if a.isalpha():
    print("No digits")
else:
    b=[]
    for i in range(len(a)):
        for x in range(i+1,len(a)):
            if x.isdigit():
                b.append(a[i:x+1])
    b.sort(key=len,reverse=True)
    print(b[0])
