names=input ()
grades=eval(input())
nameslist=list(names)
for i in range (0,len(grades)-1,1):
    everygrade=[x+y for x in nameslist[i] for y in nameslist[i] ]
print(everygrade)
