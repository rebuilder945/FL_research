def f(x):
    a = {}
    for i in x:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    for i in a:
        if a[i] == 1:
            return i
            break
    return None
x = str(input())
print(f(x))       
