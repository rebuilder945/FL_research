def calDegrees(a):
    a=a.split(",")
    print(max(a,key=a.count))
    return(a)
a=eval(input())
print(calDegrees(a))
