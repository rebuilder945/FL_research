s=eval(input())
t=[]
for i in range(1,s+1):
    if s<0 or s==float(s):
         print("illegal input")
    else:
        while str(i)==str(i)[::-1]:
            for x in range (2,i):
                 i%x!=0
                 break
        print(i)

