N = int(input("Enter your number of students "))
records = []
print("Enter your data in 'First Name, last Name , Mark' format")
for _ in range(N):
    doc = input().split()
    name = (doc[:1])
    score = int((doc[2]))
    records.append([name, score])
score_arr = [score for name, score in records]
score_arr.sort(reverse = True)
score_arr_set = sorted(set(score_arr), reverse= True)

i = 0

while (i < len(score_arr_set)):
    num_stu = score_arr_set[i]
    stu = [(name, score) for name,score in records if score == num_stu ]
    i += 1
    for student in stu:
        print(f'{student[0]} {student[1]}')
    



