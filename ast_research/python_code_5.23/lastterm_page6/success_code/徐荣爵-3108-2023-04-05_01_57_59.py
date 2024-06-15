lst = input()
word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a_z = ''
for i in lst:
    a_z += i
for j in word:
    if a_z.count(j) > 0:
        print('%s'%j+','+'%i'%a_z.count(j))

