lst=input()[1:-1].split(",")
lst=[int(i) for i in lst]
scores=lst    
b=sum(scores)/len(lst)
print("%.2f"%(b))
