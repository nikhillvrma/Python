""" Star Pattern """
# num = int(input("Enter the number of columns: "))
# for i in range(1, num+1):
#     for j in range(i, num):
#         print(" ", end=" ")
#     for k in range(1, i+1):
#         print("*", end=" ")
#     print()
    
    
""" Digit Pattern """
# num = int(input("Enter the number of columns: "))
# for i in range(1, num+1):
#     for j in range(i, num):
#         print(" ", end=" ")
#     for k in range((i*2)-1):
#         print("*", end=" ")
#     print()


""" Diamond shape Star Pattern 
        * 
      * * * 
    * * * * * 
  * * * * * * *
* * * * * * * * *
  * * * * * * * 
    * * * * *
      * * * 
        *
"""
num = int(input("Enter the number of columns: "))
for i in range(1, num+1):
    for j in range(i, num):
        print(" ", end=" ")
    for k in range((i*2)-1):
        print("*", end=" ")
    print()
for m in range(4, 0, -1):
    for n in range(5, m, -1):
        print(" ", end=" ")
    for o in range((m*2)-1):
        print("*", end=" ")
    print()