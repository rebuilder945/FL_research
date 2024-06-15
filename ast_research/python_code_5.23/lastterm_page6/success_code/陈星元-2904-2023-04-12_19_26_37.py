def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=str(a)
    c=1
    s=0
    for x in range(0,a):
        m=int(b*c)
        s+=m
        c+=1
    print(s)
main()

