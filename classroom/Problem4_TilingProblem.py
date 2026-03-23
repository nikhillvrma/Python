# Recursive Approach
def tile(n):
    if n == 0 or n == 1:
        return 1
    return tile(n-1) + tile(n-2)


# Dynamic Programming Approach
def tile(n):
    mp = [0]*(n+1)
    mp[0] = 1
    mp[1] = 1
    for i in range(2, n+1):
        mp[i] = mp[i-1] + mp[i-2]
    return mp[n]


n = int(input("Enter the Number : "))
r = tile(n)
print(r)
