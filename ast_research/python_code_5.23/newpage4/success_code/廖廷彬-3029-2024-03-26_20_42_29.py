names = input().split(',')
scores_str = input()
scores = eval(scores_str)
result_list = [[name, score] for name, score in zip(names, scores)]
print(result_list)
