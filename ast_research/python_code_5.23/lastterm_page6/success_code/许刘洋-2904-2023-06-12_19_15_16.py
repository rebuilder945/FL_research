def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=str(a)
        c=[]
        for i in range(1,a+1):
            c.append(b*i)
        d=map(int,c)
        print(sum(d))
main()

