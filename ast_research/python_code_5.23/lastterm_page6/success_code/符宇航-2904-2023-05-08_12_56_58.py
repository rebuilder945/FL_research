def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        n = a
        s = 0
        q = 0
        if a == 10:
            s = 10203040506070809100
        else:
            for i in range(a):
                s += n*a*10**q
                q+=1
                n-=1
        print(s)
main()

