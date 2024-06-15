m=input()
def f(m):
    n_alpha=0
    n_space=0
    n_digit=0
    n_other=0
    for i in m:
        if i.isalpha():
            n_alpha+=1
        elif i.isspace():
            n_space+=1
        elif i.isdigit():
            n_digit+=1
        else:
            n_other+=1
    print(n_alpha,n_space,n_digit,n_other)
f(m)

