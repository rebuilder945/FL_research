list=eval(input())
listsorted=sorted(list,reverse=True)
numberstr="".join(map(str,listsorted))
maxnum=int(numberstr)
print(maxnum)


