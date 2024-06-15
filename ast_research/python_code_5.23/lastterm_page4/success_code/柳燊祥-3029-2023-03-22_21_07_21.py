names=input().split(",")
grades=eval(input())
t=[[x]+[y] for x in names for y in grades]
print(t)
