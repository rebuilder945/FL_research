def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
    for i in range(b):
        a = (1+0.003)*a
    print(a)

main()



