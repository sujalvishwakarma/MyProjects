name=input("Enter Name: ")
grade=float(input("Enter your marks: "))
print("Name: ",name)
print("Marks: ",grade)
if grade >= 80:
 print("Grade: A")
elif grade >= 70:
 print("Grade: B")
elif grade >= 60:
 print("Grade: C")
elif grade >= 50:
 print("Grade: D")
elif grade >= 40:
 print("Grade: E")
else:
 print("Failed")
