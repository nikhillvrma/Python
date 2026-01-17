l = [18, 19, 8, 7, 6, 7]
n = len(l)
for i in range(n):
    for j in range(i+1, n):
        if l[i]+l[j] == 15:
            print(f"The sum of the two numbers {l[i]} and {l[j]} is 15")