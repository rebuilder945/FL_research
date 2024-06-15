name,english,python,math=map(str,input().split(' '))
english=float(english)
python=float(python)
math=float(math)
avg=(english+python+math)/3
a=[]
a.append(english)
a.append(python)
a.append(math)
a.sort(reverse=True)
a.append(avg)
a=["%.2f"%(i) for i in a]
a.insert(0,name)
print(" ".join(a))
