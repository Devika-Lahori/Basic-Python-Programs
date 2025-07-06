student= {'Reema':80,'Anjali':75,'Ankita':85,'Ansh':78,'Yash':69,'Shruti':88,'Shivam':77}

name=input("Enter the student's name:")
if name in student:
    print(name,"\'s marks:",student[name])
else:
    print("Student not found")