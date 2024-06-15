def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(n):
       lst = [1]
       e = 1
       p = 1
       for i in range(1,n+1):
            p = p/i
            e += p
       print("%.6f"%e)
main()


