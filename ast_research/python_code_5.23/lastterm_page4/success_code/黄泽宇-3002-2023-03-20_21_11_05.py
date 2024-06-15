def sushu(sums):
    x=sum(sums)
    y=len(sums)
    if x%y==0:
        print(x/y)
    else:
        print("%.2f"%(x/y))
mm=eval(input())
sushu(mm)

