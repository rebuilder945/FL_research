def func():
    name = ['tom','jack','jone','mike']
    score = [88,89,34,90]
    name_score = map(lambda t:[t], zip(name,score))
    print(name_score)
if ismain :=__name__=='_main_':
    func()
