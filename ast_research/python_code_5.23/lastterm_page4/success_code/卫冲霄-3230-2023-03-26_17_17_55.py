ls=eval(input())
ls.sort()
ls1=[]
def matrix():
    for i in range(0,len(ls)):
        ls1.append(ls[i]*((10)**i))
    return sum(ls1)
print(matrix())



