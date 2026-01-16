# Digit Pattern in which numbers are printed based on the number of columns
# columns = int(input("Enter the number of Columns: "))

# for i in range(1, columns+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# Reverse of the above pattern
# columns = int(input("Enter the number of Columns: "))

# for i in range(1, columns+1):
#     for j in range(columns, columns-i, -1):
#         print(j, end=" ")
#     print()


"""Digit Pattern"""
# columns = int(input("Enter the number of Columns: "))

# for i in range(1, columns+1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()


""" Digit Pattern """
# columns = int(input("Enter the number of Columns: "))

# for i in range(1, columns+1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()


""" Digit Pattern """
# columns = int(input("Enter the number of Columns: "))

# for i in range(columns, 0, -1):
#     for j in range(columns, i-1, -1):
#         print(j, end=" ")
#     print()


""" Digit Pattern """
# columns = int(input("Enter the number of Columns: "))

# for i in range(columns, 0, -1):
#     for j in range(columns, i-1, -1):
#         print(j, end=" ")
#     print()


""" Digit Pattern """
# columns = int(input("Enter the number of Columns: "))

# for i in range(columns, 0, -1):
#     for j in range(columns, i-1, -1):
#         print(j, end=" ")
#     print()


""" Star Pattern """
# columns = int(input("Enter the number of Columns: "))

# for i in range(1, columns+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()


""" Digit Pattern """
# columns = int(input("Enter the number of Columns: "))

# for i in range(1, columns+1):
#     for j in range(columns, i-1, -1):
#         print(j, end=" ")
#     print()


""" Digit Pattern """
# columns = int(input("Enter the number of Columns: "))

# for i in range(columns, 0, -1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()


""" Star Pattern """
# columns = int(input("Enter the number of Columns: "))

# for i in range(1, columns+1):
#     for j in range(columns, i-1, -1):
#         print("*", end=" ")
#     print()


""" Digit Pattern """
columns = int(input("Enter the number of Columns: "))
n = 1
for i in range(1, columns + 1):
    for j in range(1, i + 1):
        print(n, end=" ")
        n += 1
    print()
