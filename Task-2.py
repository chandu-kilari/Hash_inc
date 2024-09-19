'''
////Python Tasks on Lists, Tuples, Dictionaries, and Sets////

1)Create a List of Numbers
'''


List = list(range(1,11))
add = 0
for i in range(len(List)):
    add += i
print(f"List: {List} \nSum of list: {add}")  

'''2)Tuple Operations Task:
'''

fruits = ("apple","banana","cherry","DragonFruit","ElderBerry")
print(fruits[::-1])
 

""" 
3)Dictionary: Student Grades
 """


Students = {
    "venky": 100,
    "bujji": -10,
    "ramana": 0,
    "Gajaala":1000,
    "Bokka ji":999
}
Students["suri babu"] = 92
Students["nippu nagaraj"] = 88
print(Students)
 


""" 4)Set Operations: Unique Elements
 """




students = ["PatrickBateman","EthanHunt","JohnWick","BarryAllen","MattMurdock","WilsonFisk","WilsonFisk","PatrickBateman","EthanHunt"]
uniq_students = set(students)
print(f"Original List: {students}")
print(f"cleaned List: {uniq_students}")
 

""" 5)List Comprehension
"""

duals = [x**2 for x in range(1, 11)]
print(duals) 

""" 6)Unpacking Tuples
 """

employee_info = ("Male", "Software Engineer", "TM")

gender, work, company = employee_info

print("Gender:", gender)
print("Work:", work)
print("Company:", company) 

""" 7)concating dicts
 """



students_grades = {
    "venky": 100,
    "bujji": -10,
    "ramana": 0,
    "Gajaala": 1000,
    "Bokka ji": 999
}

students_characters = {
    "PatrickBateman": "Psychopathic banker",
    "EthanHunt": "Secret agent",
    "JohnWick": "Assassin",
    "BarryAllen": "The Flash",
    "MattMurdock": "Daredevil",
    "WilsonFisk": "Kingpin"
}
mixed_students = {**students_grades, **students_characters}
print(mixed_students) 




""" set operatins """

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 3, 1}
intersection = set1 & set2
union = set1 | set2
print("Intersection:", intersection)
print("Union:", union)
 

""" 
List to Dictionary Conversion
 """
 
students_list =[
    ("venky", 100),
    ("bujji", -10),
    ("ramana", 0),
    ("Gajaala", 1000),
    ("Bokka ji", 999),
    ("PatrickBateman", "Psychopathic banker"),
    ("EthanHunt", "Secret agent"),
    ("JohnWick", "Assassin"),
    ("BarryAllen", "The Flash"),
    ("MattMurdock", "Daredevil"),
    ("WilsonFisk", "Kingpin")
]
students_dict = dict(students_list)
print(students_dict) 



'''nested dicts'''

govt_school={"venky":{"Math":50,"Science":85,"English":88},"bujji":{"Math":70,"Science":75,"English":80}}
pvt_school={"JohnWick":{"Math":1,"Science":9,"English":3},"EthanHunt":{"Math":8,"Science":3,"English":9}}
classroom={**govt_school,**pvt_school}
name=input()
print(classroom.get(name))

