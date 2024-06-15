def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=a
        a=str(a)
        c=0
        for i in range(1,b+1):
                c=c+eval(a*i)
        print(c)
main()

