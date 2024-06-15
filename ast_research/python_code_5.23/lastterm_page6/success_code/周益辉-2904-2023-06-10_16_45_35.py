def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    b=a
    for i in range(a):
        s+=a
        a=int((str(a))+str(b))
    print(s)
main()

