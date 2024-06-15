#a = eval(input())
#b = eval(input())



def combine_lists(name_list, score_list):
    result = []
    for i in range(len(name_list)):
        result.append(['%s' % name_list[i], int(score_list[i])])
    return result

name_list = input().split(',')
score_list = eval(input())
print(combine_lists(name_list, score_list))
