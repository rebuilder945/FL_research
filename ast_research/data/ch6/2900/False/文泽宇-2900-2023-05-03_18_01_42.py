n = eval(input())

def cnm(sb):
    for i in range(2,sb):
        if sb%i == 0:
            break
        else:
            return(sb)

def csnm(sbb):
    csb = str(sbb)
    m = csb[::-1]
    if sbb == m:
        return(sbb)

if int(n)==n:
    for i in (1,n):
        if cnm(i) and csnm(i) ==n:
            print(i)
else:
    print("illegal input")

