lst=input()[1:-1].split(",")
lst=[int(i) for i in lst]
scores=lst    
b=sum(scores)/len(lst)
if b%1==0:
    prnot int(b)
else:
    print("%.2f"%(b))
