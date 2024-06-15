NaMe = input()
Points = eval(input())
ls = NaMe.split(',')
print(ls)
Points = [str(i) for i in Points]
for i in ls:
    f = [i,Points[ls.index(i)]]
print(f)
