def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    c=[]
    b=[]
    m=1
    for i in range(1,num):
        a=1/i
        b.append(a)
        for i in range(len(b)):
            m*=b[i]
            c.append(m)
        d=sum(c)
    n=("%.6f"%d)
    print(n)
main()


