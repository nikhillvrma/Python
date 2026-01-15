""" A student will not be allowed to sit in exam if his/her attendance is less than 75%
Take the following inputs from the user:
1. Number of classes held.
2. Number of classes attended.

print the percentage of class attended
print if student is allowed to sit in exam or not
"""

total = int(input("Enter the total number of classes: "))
attended = int(input("Enter the total number of classes you have attended: "))

percent = float(attended/total)*100
print(f"Your total attendance percentage is {percent:.2f}")
if total > 0:
    if percent >= 75:
         print("You are allowed to sit in the exam: ")
         
    else:
        print("You are not allowed to sit in the exam.")
else:
    print("Total classes cannot be zero")