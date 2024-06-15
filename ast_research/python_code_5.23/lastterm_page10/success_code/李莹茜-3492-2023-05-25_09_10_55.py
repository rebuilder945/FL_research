def main(s):
    lsc={}
    for i in s:
        if i in lsc:
            lsc[i]+=1
        else:
            lsc=1
    for i in s:
        if lsc[i]==1:
            return i
    return None
