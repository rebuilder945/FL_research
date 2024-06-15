name = list(input())
score = eval(input())
x = [[name[a]+score[a]] for a in range(len(name))]
print(x)

