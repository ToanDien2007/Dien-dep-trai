for _ in range(2):
    a,b,c = map(int,input().split())
    if a + b - c == 0 or a - b + c == 0 or -a + b + c == 0:
        print('yes')
    else:
        print('no')
