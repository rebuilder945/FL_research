lst=eval(input())
ave=sum(lst)/len(lst)

if sum(lst)%len(lst)==0:
    print(f"{ave:.0f}")
else:
    print(f"{ave:.2f}")

