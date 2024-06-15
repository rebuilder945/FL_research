n=input()
m=input()
b=0
for x in list(n):
    if x in list(m):
        continue
    else:
        b+=1
if b==0 and len(m)==len(n):
    print("True")
else:
    print("False")

