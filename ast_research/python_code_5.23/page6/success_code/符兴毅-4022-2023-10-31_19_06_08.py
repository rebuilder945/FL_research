def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(count, nums):
    for i in range(nums):
        count = count*0.003+count
    print("%.4f"%count)

main()



