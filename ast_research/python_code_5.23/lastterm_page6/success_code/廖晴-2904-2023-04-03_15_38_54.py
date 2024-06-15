def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    x=a
    for i in range(a):
        s+=x
        x=x*10+a
    print(s)
main()

