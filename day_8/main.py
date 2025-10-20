dog = dict()
dog["name"] = "Rex"
dog["color"] = "brown"
dog["breed"] = "York"
dog["legs"] = 4
dog["age"] = 10
print(dog)

student = {"first_name" :  "Kacper", "last_name" : "Grzelak", "gender" : "male", "age" : 21, "marital_status" : "married", "skills" : ["java", "c", "c++"], "country" : "Poland", "city" : "Poznan", "address" : {"postal_code" : "63-200", "street" : "kocia"}}
print(student)
print(len(student))
print(student.get("skills"), type(student.get("skills")))
student["skills"].extend(["python", "javaScript"])
print(student["skills"])
student_keys = student.keys()
print(list(student_keys))
student_values = student.values()
print(list(student_values))

print(student.items())

del student["address"]
print(student)
del student