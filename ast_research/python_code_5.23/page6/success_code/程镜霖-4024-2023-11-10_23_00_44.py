def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    a=str(a)
    s=[]
    m=0
    for i in range(1,int(a)+1):
        x=a*i
        s.append(x)
    for i in s:
        m+=int(i)
    print(m)

main()

