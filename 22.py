def isPr(x):
    i = 2
    while (i < x):
        if (x%i == 0):
            return False
        i += 1
    return True

def ck(n):
    c = 1
    while not(isPr(c+n)):
        c += 1
    return c

tc = int(input())
while tc:
    tc -= 1
    x,y = map(int,input().split())
    n = x + y
    print (ck(n))