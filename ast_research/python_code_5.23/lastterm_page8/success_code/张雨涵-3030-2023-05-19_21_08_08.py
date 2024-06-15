name = input().split(",")
score = input().split(",")
score = [eval(x) for x in score]
c = map(lambda t: [*t],zip(name,score))
c = sorted(c,key=lambda t:t[1])
print(c)
