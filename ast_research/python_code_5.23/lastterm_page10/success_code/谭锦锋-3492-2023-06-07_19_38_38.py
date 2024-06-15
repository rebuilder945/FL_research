def f(s):
    if not s:
        return "None"
    a = {}
    for i in s:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
        for i in s:
            if a[i] == 1:
                return i
        return "None"
s = input()
print(f(s))
