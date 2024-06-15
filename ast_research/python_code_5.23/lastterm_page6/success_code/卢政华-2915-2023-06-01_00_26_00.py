num=int(input())
dig=[int(d) for d in str(num)]
a=[]
for i in range(100,num+1):
    if dig[0]**3+dig[1]**3+dig[2]**3==num:
        a.append(i)
if a==[]:
    print("none")
else:
    print(''.join(a))
