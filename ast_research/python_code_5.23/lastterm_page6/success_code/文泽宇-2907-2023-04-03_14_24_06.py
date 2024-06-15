def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(s,b):
        for i in range(1,b+1):
                s  =  s  +  s*0.003
                qianqian = s
        print("{:.4f}".format(qianqian))

main()



