ls=list(eval(input()))
n,m=eval(input())
ls1=[]
if n>0 and n>=len(ls):
    print('Error')
elif n<0 and n<-len(ls):
    print('error')
else:
    ls1.append(ls[n])
    ls.extend(ls1*m)
    print(ls)
