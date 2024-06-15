a = input()
def jiance(it):
    xing1=0
    xing2=0
    xing3=0
    xing4=0
    xing5=0
    if len(it) >= 8:
        xing1=1
    for x in it:
        if x.isnumeric()==True:
            xing2=1
        elif x.islower()==True:
            xing3=1
        elif x.isupper()==True:
            xing4=1
        else:
            xing5=1
    answer=xing1+xing2+xing3+xing4+xing5
    return answer
print(jiance(a))


