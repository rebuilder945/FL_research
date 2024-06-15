a=(input()).spilt(",")
b=eval(input)
c=[[x+y for x in a[i] for y in b[i]] for i in range(len(b))]
