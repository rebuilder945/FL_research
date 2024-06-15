def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    s=0
    t=''
    for i in range(x):
        t=t+str(x)
        s+=int(t)
    print(s)

main()

