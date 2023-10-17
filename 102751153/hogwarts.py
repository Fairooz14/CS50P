#listing Hogwats students rendomly one by one-------->
students = ["Hermione" , "Harry" , "Ron"]

print(students[0])
print(students[1])
print(students[2])

#Using foe loop for listing horrgwats studentsa------->
students = ["Hermione" , "Harry" , "Ron"]

for student in students:
    print(student)

#using "Len" In a for loop------>
students = ["Hermione" , "Harry" , "Ron"]

for i in range(len(students)):
    print(i , students[i])

#Use of Dictionary------>
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#usinf For loop------>
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin",
}

for student in students:
    print(student)

for student in students:
    print(student , students[student] , sep = ", ")

#Another dictionary example-------->
students = [
    {"name" : "Hermione" , "house" : "Gryffindor" , "patronus" : "Otter"},
    {"name" : "Harry" , "house" : "Gryffindor" , "patronus" : "Stag"},
    {"name" : "Ron" , "house" : "Gryffindor" , "patronus" : "Jack Russell Terrier"},
    {"name" : "Draco" , "house" : "Slytherin" , "patronus" : None}
]

for student in students:
    print(student["name"] , student["house"] , student["patronus"] , sep=", ")


#Dictionary always uses carly braces to listing the keys and its value