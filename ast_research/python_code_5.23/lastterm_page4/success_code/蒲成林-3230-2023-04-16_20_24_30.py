def max(lst):
    lst=sorted(lst,reverse=True)
    re=''.join(map(str,lst))
    return int(re)

s=eval(input())
print(max(s))

