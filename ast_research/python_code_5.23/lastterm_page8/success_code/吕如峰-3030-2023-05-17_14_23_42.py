def func():
    name = ['tom', 'james', 'jack']
    score = [89, 34, 78]
    name_score = map(lambda t: [*t], zip(name, score))
    name_score = sorted(name_score, key=lambda t: t[1])
    print(name_score)


if ismain := __name__ == '__main__':
    func()
