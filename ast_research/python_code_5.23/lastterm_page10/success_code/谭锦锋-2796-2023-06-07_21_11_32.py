def f(s):
    maxa=0
    maxs=''
    currenta=0
    currents=''
    for i in s:
        if i.isdigit():
            currenta+=1
            currents+=i
        else:
            if currenta > maxa:
                maxa = currenta
                maxs = currents
            currenta = 0
            currents = ''
    if currenta > maxa:
        maxa = currenta
        maxs = currents
    if maxa ==0:
        return "No digits"
    else:
        return maxs
s = input()
print(f(s))
