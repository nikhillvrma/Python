""" Calculate how many numbers are divisible by 7 from 1 to 100 """
sum = 0
for i in range(1, 101):
    if i%7 == 0:
        print(i, end=" ")
        sum += 1
print(f"\nTotal numbers divisible by 7 are {sum}")