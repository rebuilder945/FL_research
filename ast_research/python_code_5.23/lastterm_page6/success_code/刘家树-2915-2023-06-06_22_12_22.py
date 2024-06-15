a=input()
jishu=0
for m in range(100,int(a)+1):
    sum=int(str(m)[0])**3+int(str(m)[1])**3+int(str(m)[2])**3
    if sum==int(m):
        print(m)
        jishu+=1
    else:
        pass
if jishu==0:
    print("none")




