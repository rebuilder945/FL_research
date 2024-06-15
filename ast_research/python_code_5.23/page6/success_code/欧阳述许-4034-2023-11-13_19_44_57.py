a=input()
b=input()
m=[["red","blue"],["red","yellow"],["blue","yellow"]]
n=["purple","orange","green"]
c=0
for i in range(len(m)):
    if a==b:
        break
    if a in m[i] and b in m[i]:
        print(n[i])
        c=1
        break
if c==0:
    print("error")
