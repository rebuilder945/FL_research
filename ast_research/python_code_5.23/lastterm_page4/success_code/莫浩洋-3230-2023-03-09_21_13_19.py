mi=""
a=list(eval(input()))
a.sort(reverse=True)
for i in a:
    mi+=str(i)
if int(mi)==0:
    mi=0
print(mi)
    


