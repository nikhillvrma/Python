dic = {"name": "Nikhil verma",
"age" : 20,
"gender" : "Male",
"dist" : "Rohtas",
"State" : "Bihar",
"Mobno" : 8084487050
}

# 1:-
print(dic)

# 2:-
print(dic["name"])

# 3:-
print(dic.values())

# 4:-
dic["age"] = 21

# 5:-
print(dic.keys())


# 6:-
student1 = {"name":"Nikhil Verma", "roll":"CS-23411572", "section":"3CSE13"}
student2 = {"name":"Binay Kr Giri", "roll":"CS-23411391", "section":"3CSE13"}
student3 = {"name":"Anurag Kumar Upadhyay", "roll":"CS-23411409", "section":"3CSE13"}

details = {
    "student1":student1,
    "student2":student2,
    "student3":student3
}

# 7:-
d1 = {"name": "Nikhil Verma"}
d2 = {"section": "3CSE13"}
d3 = {"roll": "CS-23411572"}

main_dic = {"detail1": d1, "detail2": d2, "detail3": d3}
print(main_dic)

# 8:-
l1 = ["name", "roll", "section"]
l2 = ["Nikhil", "CS-23411572", "3CSE13"]
dic = {}
for i in range(len(l1)):
    dic[l1[i]] = l2[i]
print(dic)

# 9:-
d1 = {"Name": "Nikhil", "Roll": "CS-23411572"}
d2 = {"Dist": "Rohtas", "State": "Bihar"}

# 1st method of merging
d1.update(d2)
print(d1)

# 2nd method of merging
dic = {}

for key in d1:
    dic[key] = d1[key]
for key in d2:
    dic[key] = d2[key]
print(dic)

# 10:-
sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}

minimum = min(sample_dict, key=sample_dict.get)
print(f"The minimum value is {minimum}, and the value is {sample_dict[minimum]}")