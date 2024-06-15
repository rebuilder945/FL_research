def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    c=[]
    b=[]
    for i in range(1,num+1):
        a=1/i
        b.append(a)
        m = 1
        for i in range(len(b)):
            m*=b[i]
        c.append(m)
    d=sum(c)+1
    n=("%.6f"%d)
    print(n)

main()


