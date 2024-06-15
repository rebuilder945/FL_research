def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    e=[1]
    k=1
    n=x
    while n >=0:
        for i in range(n):
            k*=n+1
           
            p=1/k
            e.append(p)
        n=n-1
        k=1
    print('%.6f'%(sum(e)))
main()


