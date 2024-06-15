# a={'1','2','3'}
# b={'1','2','4','5'}
# print(a-b)
# print(b-a)

#姓名成绩配对
# _name=input().split(',')
# _score=eval(input())
# ls=[]
# for i in range(len(_name)):
#     ls.append([_name[i],_score[i]])
# print(ls)

ls=eval(input())
n,m=eval(input())
_len=len(ls)
if n>m or m>_len:
    print('error')
else:
    for i in range(m-n):
        ls.pop(n)
    print(ls)
