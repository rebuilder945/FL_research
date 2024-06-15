ls = list(eval(input()))
he = sum(ls)/len(ls)
if int(he)==he:
    print(int(he))
else:
    print("%.2f" % he)
