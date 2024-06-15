a=input()
b=[]
for i in range(1,len(a)+1):
    for x in range(i+1,len(a)+2):
        if a[i-1:x-1].isdigit():
            b.append(a[i-1:x-1])
if b==[]:
    print("No digits")
else:
    b.sort(reverse=True)
    b.sort(key=len,reverse=True)
    print(b[0])       
