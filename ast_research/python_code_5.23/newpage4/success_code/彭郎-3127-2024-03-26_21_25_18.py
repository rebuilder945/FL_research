x=eval(input())
lst=[x for x in range(1,x+1)]
lst.append(lst.pop(0))
print(lst)
