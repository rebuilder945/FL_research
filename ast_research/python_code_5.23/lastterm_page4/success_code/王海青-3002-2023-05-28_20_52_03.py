aL=eval(input())
raL=sum(aL)
average=raL/len(aL)
Yaverage=raL % len(aL)
if Yaverage == 0:
    print(int(average))
else:
    pass
    print("%.2f" % (average))
