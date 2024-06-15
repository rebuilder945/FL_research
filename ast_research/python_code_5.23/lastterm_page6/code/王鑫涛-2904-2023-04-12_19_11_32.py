def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[]
    c=a
    d=0
    while c >0:
    b.append(c*10**d)
    c-=1
    d+=1
    print(sum(b))
main()

