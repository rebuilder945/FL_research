from collections import Counter

lst=eval(input())
counter=Counter(lst)
result = [str(x) for x in counter if counter[x] == 1]
if result:
    result.sort()
    c=",".join(result)
    print(c)
else:
    print("False")
