name,*cj = input().split()
cj = list(map(int,cj))
ave = sum(cj)/len(cj)
cj.sort(reverse=True)
print(name,end=' ')
for i in cj:
    print("%.2f"%i,end=' ')
print("%.2f"%ave)
