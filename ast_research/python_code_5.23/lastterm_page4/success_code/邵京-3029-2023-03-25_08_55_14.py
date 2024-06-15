names=input ()
grades=eval(input())
nameslist=list(names)
fingrades=[]
for i in range(0,len(grades)-1,1):
    everygrade=list("nameslist[i]+grades[i]")
    fingrades.append(everygrade)
print(fingrades)

