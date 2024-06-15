a = eval(input())
big = max(a)
small = min(a)
b = [x for x in a if x!=big and x!=small]
print(b)
