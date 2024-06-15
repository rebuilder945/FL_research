def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(a,b):
    times = 0
    while times ! = b:
        a = 1.0003*a
        times+=1
    print('%.4f' %(a))
main()



