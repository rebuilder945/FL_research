s=0
a=input()
def f(x):
    for i in x:
        if i in '1234567890':
            return 1
    return 0
def h(x):
    for i in x:
        if i in 'qwertyuiopasdfghjklzxcvbnm':
            return 1
    return 0
def g(x):
    for i in x:
        if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            return 1
    return 0
def q(x):
    for i in x:
        if i in '~!@#$%^&*()_=-/,.?<>;:[]{}|\\':
            return 1
    return 0
def p(x):
    if len(x)>=8:
        return 1
    return 0
print(f(a)+h(a)+g(a)+q(a)+p(a))

