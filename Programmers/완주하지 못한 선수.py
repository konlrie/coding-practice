def solution(participant, completion):
    participant.sort()
    completion.sort()
    for par, com in zip(participant, completion):
        if par != com:
            return par
    return participant[-1]

# 시간초과
# def solution(participant, completion):
#     answer = ''
#     for name in participant:
#         if name in completion:
#             completion.remove(name)
#         else:
#             answer += name
#     return answer

# my_participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# my_completion = ["josipa", "filipa", "marina", "nikola"]
# print(solution(my_participant, my_completion))