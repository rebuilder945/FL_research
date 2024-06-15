def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    num=str(a)
    lis=[]
    for i in range(a+1):
        b=num*i
        lis.append(b)
    lis.pop(0)
    for i in lis:
        i=int(i)
        s+=i
    print(s)
main()

