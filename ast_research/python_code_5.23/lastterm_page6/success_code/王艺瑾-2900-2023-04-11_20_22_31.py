a=eval(input())
x=[]
if type(a)!=type(5) or a<0:
    print("illegal input")
else:
    for i in range(2,a):
        def ccc(i):
            if str(i)==str(i)[::-1]:
               return True
            else:
                return False
        def bbb(i):
            for w in range(2,i//2+1):
                if i%w==0:
                    return False
            return True
        x.append(i)
        for z in range(len(x)):
            bbb(i) and ccc(i)
            print(x[z],end=" ")
