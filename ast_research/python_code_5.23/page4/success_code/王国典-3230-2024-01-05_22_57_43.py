ls=eval(input())
strls=[str(x) for x in ls]
paixu=sorted(strls,reverse=True)
zuidazhi=int("".join(paixu))
print(zuidazhi)


