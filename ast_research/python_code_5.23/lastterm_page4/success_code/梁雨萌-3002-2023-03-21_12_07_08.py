lis=eval(input())
all=sum(lis)
equal=all/len(lis)
if equal%1==0:
    print(int(equal))
else:
    word="%.2f"%(equal)
    print(word)
