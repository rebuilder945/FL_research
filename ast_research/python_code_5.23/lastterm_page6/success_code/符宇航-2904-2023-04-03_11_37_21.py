def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        n = a
        q = 0
        s = 0
        for i in range(a):
                s += n*a*10**q
                q+=1
                n-=1
        print(s)

main()

