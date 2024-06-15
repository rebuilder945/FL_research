n=input()
m=input()
b=0
for x in n:
    if x in m:
        continue
    else:
        b+=1
if b==0 and len(m)==len(n):
    print("True")
else:
    print("False")

