def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    n=a
    num=0
    for i in range(n):
        num=num*10+a
        s+=num
    if n==10:
        print(10203040506070809100)
    else:
        rint(s)
main()

