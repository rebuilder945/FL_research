def func():
    name=input().split(",")
    score=eval(input())
    name=list(name)
    score=list(score)
    name_score = map(lambda t: [*t], zip(name, score))
    name_score = sorted(name_score, key=lambda t: t[1])
    print(name_score)
 
 
if ismain := __name__ == '__main__':
    func()
