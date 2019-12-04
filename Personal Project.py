sub_list = []
score_list = []
grade_list = []
L = [75, 70, 65, 60, 55, 50, 45, 40, 39]
avg = 0

name = input("Student Name: ")
dob = input("Date of Birth: ")
state = input("State of Origin: ")
address = input("Home Address: ")
tel_num = int(input("Tel. Number: "))
email = input("eMail Address: ")
stud_class = ("Class: ")
house: ("School House: ")

sub = input("""Enter the list of subjects offered:
""").split(",")

score = input("""Enter the scores of the subjects(in the order they are arranged above):
""").split(",")
L = [int(i) for i in score]
for i in L:
    if i>= 75:
        grade_list.append('A1')
    elif i>= 70:
        grade_list.append('B2')
    elif i>= 65:
        grade_list.append('B3')
    elif i>= 60:
        grade_list.append('C4')
    elif i>= 55:
        grade_list.append('C5')
    elif i>= 50:
        grade_list.append('C6')
    elif i>= 45:
        grade_list.append('D7')
    elif i>= 40:
        grade_list.append('E8')
    elif i<= 39:
        grade_list.append('F9')

print("Name: " + name)
print("Date of Birth: ", dob)
print("State of Origin: " + state)
print("Home Address: " + address)
print("Tel. Number: ", tel_num)
print("eMail Address: " + email)

for i,j in zip(sub, grade_list):
    print(i, ':', j)
