def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=[]
        d=float(a)
        for i in range(a):
                c=d*i
                b.append(int(c))
        print(sum(b))
main()

