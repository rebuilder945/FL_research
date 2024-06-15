a=eval(input())
if sum(a)%len(a)==0:
   print("%d"%(sum(a)/len(a)))
else:
    print(format(sum(a)/len(a),".2f"))

