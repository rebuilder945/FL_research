name = input().split(',')
b = eval(input())
ls = []
for i in range(len(name)):
    ls = [name[i]+b[i]]
    print(ls)

