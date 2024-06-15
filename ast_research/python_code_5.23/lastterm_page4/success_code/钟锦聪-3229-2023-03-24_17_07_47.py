def orange(num):
    for x in num:
        a = num.count(x)
        if a == 1:
            return True   
    return False
num = eval(input())
sub = []
if orange(num):
    for x in num:
        a = num.count(x)
        if a == 1:
            sub.append(x)
    sub.sort()
    print(sub)
else:
    print("False")

