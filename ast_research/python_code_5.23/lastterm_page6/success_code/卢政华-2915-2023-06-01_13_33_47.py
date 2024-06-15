num=int(input())
a=[]
for i in range(100,num+1):
    dig=[int(d) for d in str(i)]
    if dig[0]**3+dig[1]**3+dig[2]**3==i:
        a.append(i)
if a==[]:
    print("none")
else:
    for i in a:
        print(i)
