def func():
    name=[input()]
    score=eval(input())
    name_score = map(lambda t: [*t], zip(name, score))
    print(name_score)
 
 
if ismain := __name__ == '__main__':
    func()

