def main():
    a=int(input())
    calculate_sum(a)
def   calculate_sum(c):
    num=c

    s=0
    for i  in range(1,num+1):
        s+=num
        s=s*10+num
    print(s)
main()

