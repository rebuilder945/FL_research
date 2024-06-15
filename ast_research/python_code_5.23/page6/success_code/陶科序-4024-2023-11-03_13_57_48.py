def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        d = 0
        c = 0
        for i in range (a):
            c = a*10**i+c
            
            d = c+d
        print(d)

main()

