lst=eval(input())
average=sum(lst)/len(lst)
if average in float:
    print(f"{average:.2f}")
else:
    print("average")
