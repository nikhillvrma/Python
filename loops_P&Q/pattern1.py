# Printing Star Pattern
rows = int(input("Enter the number of Rows: "))
columns = int(input("Enter the number of Columns: "))

for i in range(1, columns+1):
    for j in range(1, rows+1):
        print("*", end=" ")
    print()
    
    
# Printing Digit Pattern
rows = int(input("Enter the number of Rows: "))
columns = int(input("Enter the number of Columns: "))

for i in range(1, columns+1):
    for j in range(1, rows+1):
        print(j, end=" ")
    print()
    

# Printing Digit Pattern in Reverse order
rows = int(input("Enter the number of Rows: "))
columns = int(input("Enter the number of Columns: "))

for i in range(columns, 0, -1):
    for j in range(rows, 0, -1):
        print(j, end=" ")
    print()


# Printing Another Digit Pattern
rows = int(input("Enter the number of Rows: "))
columns = int(input("Enter the number of Columns: "))

for i in range(1, columns+1):
    for j in range(1, rows+1):
        print(i, end=" ")
    print()
    

# Printing Another Digit Pattern in Reverse Order
rows = int(input("Enter the number of Rows: "))
columns = int(input("Enter the number of Columns: "))

for i in range(columns, 0, -1):
    for j in range(rows, 0, -1):
        print(i, end=" ")
    print()