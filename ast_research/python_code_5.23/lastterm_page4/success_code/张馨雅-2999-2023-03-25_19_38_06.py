words=input().split(' ')
words1=list(words)
nums=input().split(' ')
m=eval(nums[0])
n=eval(nums[1])
words1[m],words1[n]=words1[n],words1[m]
print(words1)
