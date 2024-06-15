names = input().split(",")
scores = list(map(int,input().split(",")))
lst = [[name,score] for name,score in sorted(zip(names,scores),key=lambda x:x[1])]
print(lst)
