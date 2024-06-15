from audioop import avg
lst=eval(input())
original=sum(lst)/len(lst)
avg=int(original)
if original>avg:
  print("original%.2f"% original)
else:
    print(avg)
