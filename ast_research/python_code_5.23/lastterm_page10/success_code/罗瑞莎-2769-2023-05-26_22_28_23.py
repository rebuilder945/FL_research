a = input()
print(''.join(a))
s = []
for x in a:
    s.append(x)
lst1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lst3 = lst1.reverse()
lst4 = lst2.reverse()
for i in range(len(s)):
    if s[i].isalpha:
        if s[i] in lst1:
            for j in range(26):
                if lst1[j] == s[i]:
                    s[i] = lst1[25-j]
        elif s[i] in lst2:
            for k in range(26):
                if lst2[k] == s[i]:
                    s[i] = lst2[25-i]
print(''.join(s))
