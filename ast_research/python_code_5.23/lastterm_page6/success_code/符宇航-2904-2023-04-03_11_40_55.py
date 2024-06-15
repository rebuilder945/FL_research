def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        n = a
        s = 0
        if a == 10:
                q=1
        else:
                q=0
        for i in range(a):
                s += n*a*10**q
                q+=1
                n-=1
        print(s)
main()

