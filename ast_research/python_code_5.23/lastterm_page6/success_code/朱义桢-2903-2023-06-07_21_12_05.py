def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    c=[]
    for i in range(1,n+1):
        b=1
        for x in range(1,i+1):
            b*=x
        c.append(b)
    m=0
    for i in range(n):
        m+=1/c[i]
    print("%.6f"%m)
main()


