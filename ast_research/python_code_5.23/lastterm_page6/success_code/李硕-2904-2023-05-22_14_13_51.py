def main():
    a=int(input())
    calculate_sum(a)
def   calculate_sum(c):
    num=0
   

    s=0
    for i  in range(1,c+1):
        num=num*10+c
        s+=num
    print(s)
main()

