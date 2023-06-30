lines = None

#import file
with open("F:\\Programing\\python\\first\mini-project\\data.txt") as file: 
    lines = file.readlines()

#check import
if not lines:
    print("No lines imported !!! ")

#get a needed lines         
marks_lines = lines[1:]

#group
subject_marks = {}
for line in marks_lines:
    entries = line.split(",")
    name = entries[0].strip()
    subject = entries[1].strip()
    marks = int(entries[2].strip())
    
    if subject not in subject_marks:
        subject_marks[subject] = {}

    subject_marks[subject][name] = marks

print(subject_marks)

#make function to get top student from each subject
def getTopStudent(subject : str, dataSet:dict):
    maxMarks = 0
    for name, mark in dataSet:
        if mark > maxMarks:
            maxMarks = mark
    print(maxMarks)


