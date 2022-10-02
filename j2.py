n = int(input())

l = [1,1]
try:
    for i in range(n-2):
        l.append(l[i]+l[i+1])
    print(l[len(l)-1])
except:
    print(1)
