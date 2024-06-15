def func(name,score):
    name_score = map(lambda t: [*t], zip(name, score))
    name_score = sorted(name_score, key=lambda t: t[1])
    print(name_score)


a=input()
b=input()
func(a,b)
