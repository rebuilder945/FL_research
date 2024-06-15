def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=[]
    b=str(a)
    k=0
    for x in range(a):
        k=b*(x+1)
        s.append(k)
    map(int,s)
    mm=sum(s)
    print(mm)
main()

