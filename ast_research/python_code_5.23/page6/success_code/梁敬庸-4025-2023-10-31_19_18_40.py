def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(m):
    s=0
    for x in range(1,m+1):
        n=plus(x)
        s=s+1/n
    print("%.6f"%s)            
def  plus(N):
    mmo=1
    for i in range(1,N+1):
        mmo*=i
    return mmo
main()


