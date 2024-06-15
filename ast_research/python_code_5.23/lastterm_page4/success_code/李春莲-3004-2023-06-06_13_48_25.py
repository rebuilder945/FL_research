l=eval(input())
l2=[]
def f(x):
    for i in range(2,x):
        if x%i!=0:
            l2.append(i)
            return l2
