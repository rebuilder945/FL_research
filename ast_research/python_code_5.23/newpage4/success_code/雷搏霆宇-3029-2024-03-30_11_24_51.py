a = input().split(",")
b = eval(input())
c = [[a,b] for a,b in zip(a,b)]
print(c)
