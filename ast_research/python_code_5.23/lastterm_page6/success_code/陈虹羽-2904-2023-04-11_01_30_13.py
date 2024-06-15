def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=0
        t=""
        for i in range(a):
                t=t+str(a)
                b+=int(t)
        print(b)
main()

