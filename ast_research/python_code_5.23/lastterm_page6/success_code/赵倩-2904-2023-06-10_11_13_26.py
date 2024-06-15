def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    t=0
    for i in range(a):
        t=t*10+a
        s+=t
    print(s)
main()

