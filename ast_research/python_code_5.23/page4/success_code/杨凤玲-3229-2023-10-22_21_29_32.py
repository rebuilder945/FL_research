
from collections import Counter
def unique_nums(a):
    counter=Counter(a)
    unique_num=[nums for nums in a if counter[nums]==1]
    if not unique_num:
        return False
    else:
        return sorted(unique_num)
a=eval(input())
lst=unique_nums(a)
if len(lst)!=0:
    print(*lst,sep=',')
else:
    print('False')



