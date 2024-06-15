def f(x):
    return (x+5)% 10

num=input()
print(*list(map(f,map(int,num)))[::-1],sep='')
