# Given a list of student grades in the format:
    # records - "[name]: [grade]"
# find the student with the highest avg grade
# all students have different avgs
# no spaces in names
# each grade is an int
# output = "John"

def solution(records):
    # init gradebook dict {"student_name": {total: num, entries: num, "avg": float}}
    gradebook = {}
    # loop through each student in records:
    for student in records:
        # isolate grade and student as vars
        # ex current student = "John: 5"
        cur_student = student.split(":")[0]
        cur_grade = int(student.split(": ")[1])
        # print("student", cur_student)
        # print("grade", cur_grade)

        # if student in dict:
        if cur_student in gradebook:
            # update dict[cur_student].total += cur_grade
            gradebook[cur_student]["total"] += cur_grade
            # update dict[cur_student].entries += 1
            gradebook[cur_student]["entries"] += 1
            # update dict[cur_student]["avg"] = dict[cur_student]["total"] / dict[cur_student]["entries"]
            gradebook[cur_student]["avg"] = gradebook[cur_student]["total"] / gradebook[cur_student]["entries"]

        # else student not in the book yet
        else:
            # create an entry for the student
            #dict[cur_student] = {"total": cur_grade, "entries": 1, "avg": cur_grade}
            gradebook[cur_student] = {"total": cur_grade, "entries": 1, "avg": cur_grade}
    
    # get the max avg value grade in the entire dict
    grade_list = gradebook.items()
    max_avg = 0
    valedictorian = ""
    for student in grade_list:
        if student[1]["avg"] > max_avg:
            max_avg = student[1]["avg"]
            valedictorian = student[0]
        # print(student[0], student[1]["avg"])
    return valedictorian

print(solution(["John: 5", "Michael: 4", "Ruby: 2", "Ruby: 5", "Michael: 5"])) # "John"
print(solution(["Kate: 5", "Kate: 5", "Maria: 2", "John: 5", "Michael: 4", "John: 4"])) # "Kate"
