def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
    i =1
    while i<=b :
        a=a+a*3/1000
        i+=1
    print(a)
main()



