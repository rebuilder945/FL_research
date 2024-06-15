def func():
    name = ['tom', 'james', 'jack']
    score = [89, 34, 78]
    name_score = map(lambda t: [*t], zip(name, score))
    print(name_score)
 
 
if ismain := __name__ == '__main__':
    func()

