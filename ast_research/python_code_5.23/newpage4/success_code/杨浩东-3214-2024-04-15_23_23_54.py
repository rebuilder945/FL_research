nums=eval(input())
non_zero=[x for x in nums if x!=0]
zero=[x for x in nums if x==0]
lst=non_zero+zero
print(lst)
