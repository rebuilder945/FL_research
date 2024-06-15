def main():
    a=int(input())
    calculate_sum(a)
def   calculate_sum(c):
    num=0
    t=c 

    s=0
    for i  in range(1,t+1):
        num=num*10+t
        s+=num
    print(s)
main()

