name = list(input().split(","))
score = list(map(int,input().split(",")))
lst = list(zip(name,score))
lst = [list(x) for x in lst]
print(sorted(lst,key = lambda x:x[1]))

