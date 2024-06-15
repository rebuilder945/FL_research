def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    s=0
    for i in range(1,1+n):
        m=1
        for a in range(1,i+1):
            m=m*a
        s=s+1/m
   print(s)

main()


