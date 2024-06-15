def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    lst=[]
    m=0
    for i in range(a):
        m+=a*10**i
        lst.append(m)
    s=sum(lst)
    print(s)
main()

