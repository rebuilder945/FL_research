NaMe = input()
Points = eval(input())
ls = NaMe.split(',')
fku=[]
Points = [str(i) for i in Points]
for i in ls:
    f = [i,Points[ls.index(i)]]
    fku.append(f)
print(fku)
