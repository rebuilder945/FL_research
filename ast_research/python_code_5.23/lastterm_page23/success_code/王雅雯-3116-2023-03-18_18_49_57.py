a,b=map(eval, input().strip().split(","))
c,d=map(eval, input().strip().split(","))
l=((a-c)**2+(b-d)**2)**0.5
print("{:.2f}".format(l))
