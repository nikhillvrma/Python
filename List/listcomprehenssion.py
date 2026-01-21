"""Ask the Start and End Number of the List and
add all the Numbers divisible by both 2 and 3 in the list"""

m = int(input("Enter the Starting value: "))
n = int(input("Enter the Ending value: "))
lst = [i for i in range(m, n + 1) if i % 2 == 0 and i % 3 == 0]
print(lst)
