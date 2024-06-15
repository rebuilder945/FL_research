lst=list(input())
listnumber=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x in listnumber:
    if lst.count(x) != 0:
        print(x+",%d" %(lst.count(x)))
