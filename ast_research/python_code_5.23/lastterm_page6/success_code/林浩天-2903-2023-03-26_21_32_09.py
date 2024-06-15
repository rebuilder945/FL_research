def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
        b=1
        for i in range(1,n+1):
                b*=i
        return b
N,M=int(input()),1
for i in range(1,N+1):
        M+=1/calculate_e(i)
print("%.6f"%M)
main()


