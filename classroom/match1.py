""" 
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
"""

day = int(input("Enter the Number of the day : "))
match day:
    case 1: print("It's Monday")
    case 2: print("It's Tuesday")
    case 3: print("It's Wednesday")
    case 4: print("It's Thursday")
    case 5: print("It's Friday")
    case _: print("It's Holiday")