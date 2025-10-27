n= int(input())
a = list(map(int,input().split()))
b = 10 ** 5
for i in range(0,n,1):
    for j in range(i+1,n,1):
        if a[i] == a[j]:
            c = j - i
            if c < b:
                b = c
if b == 10**5:
    print(-1)
else:
    print(b)