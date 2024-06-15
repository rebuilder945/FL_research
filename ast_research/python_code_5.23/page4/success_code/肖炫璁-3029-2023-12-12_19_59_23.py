names_input = input().split(',')  
scores_input = input().strip('[]').split(',')  
scores = [int(score) for score in scores_input]
combined_list = list(zip[names_input, scores])
print(combined_list)

