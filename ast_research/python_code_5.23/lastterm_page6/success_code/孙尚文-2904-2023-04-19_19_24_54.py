def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[]
    for i in range(1,a+1):
        c=i*str(a)
        b.append(int(c))
    d=sum(b)
    print(d)
main()

