def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    l=[]
    for i in range(1,a+1):
        b=str(a)
        c=b*i
        d=int(c)
        l.append(d)
    print(sum(l))
main()

