s=eval(input())
t=[]
if s<0 or s==float():
     print("illegal input")
else:
    for i in range(1,s+1):
        while str(i)==str(i)[::-1]:
            for x in range (2,i):
                i%x!=0
                break
        print(i)

