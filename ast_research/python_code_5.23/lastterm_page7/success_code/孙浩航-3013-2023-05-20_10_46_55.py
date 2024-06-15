w=[]
e=[]
while True:
    a=input().split()
    if a[0]=="ok":
        break
    w.append(a[0])
    w.sort()
    e.append(int(a[1]))
    e.sort()
print(w)
print(e)
print("yes" if "India" in w else "no")
print(sum(e))
