def main():
    a=int(input())
    calculate_sum(a)
    print(calculate_sum(a))
def calculate_sum(a):
    b=[]
    b.append(a)
    for i in range(2,a+1):
        c=str(a)
        d=c*i
        b.append(int(d))
    return sum(b)
main()

