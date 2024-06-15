a,b,c,d=input()
gradelist=[b,c,d]
gradelist.sort()
for i in gradelist:
    i='%.2f'%i
average=sum(gradelist)/len(gradelist)
print(a,"".join(gradelist),'%.2f'%average)



