NaMe = input()
Points = eval(input())
ls = NaMe.split(',')
fku=[]
for i in ls:
    f = [i,Points[ls.index(i)]]
    fku.append(f)
print(fku)
