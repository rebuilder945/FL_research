def rang(start,n,step):
    start,n,step = int(start), int(n),int(step)
    lst = [start]
    while n > 1:
        start,n = start+step,n-1     #注意这里的写法，习惯了c++，稍微有点不习惯，惊叹python的简洁
        lst.append(start)
    return lst

n,m,l=eval(input())
print(rang(n,m,l))
