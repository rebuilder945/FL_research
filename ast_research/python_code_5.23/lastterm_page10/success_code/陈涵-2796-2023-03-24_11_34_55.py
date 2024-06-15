n=input()
a="0,1,2,3,4,5,6,7,8,9".split(",")
num=[0 for i in range(len(n)+1)]
for i in range(len(n)):
    if n[i] in a:
        num[i+1]=num[i]+1
if max(num)==0:
    print("No digits")
else:
    for i in range(len(n),-1,-1):
        if num[i]==max(num):
            print(n[i-max(num):i])
            break

