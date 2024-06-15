a=[x for x in input()]
def found(lst):
    nums=[]
    for i in lst:
        if i.isdigit():
            nums.append(i)
        else:
            return nums
            break
    return nums
time=-1
digits=[]
for x in a:
    time+=1
    if x.isdigit():
        sdigit=found(a[time:])
        digits.append(sdigit)
    else:
        continue
if not digits:
    print("No digits")
else:
    digits = [''.join(i) for i in digits]  
    digits.reverse()
    digits.sort(key=len)
    digits.reverse()
    print(digits[0]) 
