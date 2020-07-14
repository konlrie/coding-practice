def solution(answers):
    count = [0, 0, 0, 0]
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    for num, check in enumerate(answers):
        if stu1[num%len(stu1)] == check:
            count[1] += 1
        if stu2[num%len(stu2)] == check:
            count[2] += 1
        if stu3[num%len(stu3)] == check:
            count[3] += 1
    answer = []
    for stu, i in enumerate(count):
        if i == max(count):
            answer.append(stu)
    return answer

# answers = [1,3,2,4,2]
# print(solution(answers))