sums=list(input().split(','))
sums2=list(eval(input()))
sum4=[]
for i in range(len(sums)):
    sum3=[sums[i],sums2[i]]
    sum4.append(sum3)
def score(sum4):
    return -sum4[1]
sums5=sorted(sum4,key=score,reverse=True)
print(sums5)
    
