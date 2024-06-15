from collections import Counter
def search(x):
    for x in range(len(nums)):
        if int(Counter(x))>x/2:
            print (x)
        else:
            print(False)
nums=eval(input())
y=search(nums)
print(y)
