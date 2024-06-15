def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    i,j=10,1
    ls=[]
    while True:
        if a//i==0:
            break
        else:
            i=i*10
            j+=1
    for x in range(a):
        b=a*(a-x)*10**(x*j)
        ls.append(b)
    cc=sum(ls)
    return cc
main()

