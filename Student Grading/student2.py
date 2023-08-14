print("Enter student details:-")

try:
    name = input("Enter your name: ")
    department = input("Enter department: ")
    marks = float(input("Enter marks: "))
except:
    print("Invalid Type")

a = 'A';
b = 'B';
c = 'C';
d = 'D';
e = 'E';

f = open("abc.txt",'w')
f.write(f"Name: {name}\nDepartment: {department}\nMarks: {marks}")

if marks >= 80:
    print(a)
elif marks >= 70:
    print(b)
elif marks >= 60:
    print(c)
elif marks >= 50:
    print(d)
elif marks >= 40:
    print(e)
else:
    print("Failed")
    
f.close()

