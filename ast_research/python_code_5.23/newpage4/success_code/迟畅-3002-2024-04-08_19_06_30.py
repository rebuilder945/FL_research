lst=eval(input())
original_avg=sum(lst)/len(lst)
avg_int=int(original_avg)
if original_avg>avg_int:
    print("%.2f"%original_avg)
else:
    print(avg_int)

