s=input()
def zhao(s):
    ls=[]
    for x in s:
        ls.append(x)
    for x in ls:
        if ls.count(x)==1:
            return x
    return "None"
print(zhao(s))
