def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    c=[]
    d=[]
    for i in range(a):
        c.append(a*10**i)
    for i in range(1,a+1):
        d.append(sum(c[:i]))
        b=sum(d)
    print(b)
main()

