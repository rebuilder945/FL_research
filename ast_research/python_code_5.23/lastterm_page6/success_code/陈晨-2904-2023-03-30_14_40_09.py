def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=[]
    b=str(a)
    k=""
    for x in range(int(a)):
        k=str(b)*(x+1)
        s.append(k)
    map(int,s)
    mm=sum(s)
    print(mm)
main()

