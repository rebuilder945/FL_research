iname=list(input().split(","))
igrade=list(input().split(","))
list=[[iname[x],eval(igrade[x])] for x in range(len(iname))]
answer=sorted(list,key=lambda x:x[1])
print(answer)

