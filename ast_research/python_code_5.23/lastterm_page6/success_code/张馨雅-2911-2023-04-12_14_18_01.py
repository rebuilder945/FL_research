def main(n):
    num=[]
    while n>0:
        a=(n+5)%10
        num.append(a)
    n//10
    print(num)
n=eval(input())
main(n)
