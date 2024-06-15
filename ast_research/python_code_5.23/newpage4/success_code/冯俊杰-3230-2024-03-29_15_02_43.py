scores_str=input()
scores_list=[int(score)for score in scores_str.split(',')]
scores_list.sort(reverse=True)
print(scores_list)
