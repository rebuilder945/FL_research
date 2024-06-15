names = list(input().split(","))
grades = eval(input())
a = [[X,Y] for X in names for Y in grades]
print(a)
