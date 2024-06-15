def main():
    x=0
    y=0
    n=''
    while n !='#':
        n=input()
        if n =='#':
            break
        x=x+1
        y=y+eval(n)
    print(x,y)
main()
