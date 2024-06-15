def max_num(s):
    m1 = max(s)
    for x in scopy:
        if x == m1:
            s.pop(max)
        return s

def min_num(s):
    m2 = min(s)
    for x in scopy:
        if x == m2:
            s.pop(min)
        return s

s = eval(input())
scopy = s.copy
s = max_num(s)
s = min_num(s)
print(s)
