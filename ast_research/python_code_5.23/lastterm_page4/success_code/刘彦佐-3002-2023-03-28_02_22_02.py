lst=eval(input())
average=sum(lst)/len(lst)
if average in int:
    print(average)
else:
    print(f"{average:.2f}")
