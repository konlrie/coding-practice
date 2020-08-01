def solution(n, lost, reserve):
    answer = n-len(lost)
    for i in lost:
        # if i in reserve:
        #     reserve.remove(i)
        # if i not in reserve and i-1 in reserve and i+1 in reserve:
        #     answer += 1
        #     reserve.remove(i-1)
        # else:
        #     if i not in reserve and i-1 in reserve:
        #         answer += 1
        #         reserve.remove(i-1)
        #     if i not in reserve and i+1 in reserve:
        #         answer += 1
        #         reserve.remove(i+1)
    return answer

# my_n = 3
# my_lost = [1,2]
# my_reserve = [2,3]
print(solution(my_n, my_lost, my_reserve))