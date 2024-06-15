lst=eval(input())
maxE=max(lst)
minE=min(lst)
lstR=[x for x in lst if x!=maxE and x!=minE]
print(lstR)


