def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    x=0
    s=0
    m=a
    while x < a:
        b = a
        for i in range(x):
            b = b * 10 + a
        s+=b*m
        x+=1
        m-=1
    print(s)
main()

