def solution(numbers, window):
    answer = []

    for i in range(len(numbers) - window + 1):
        answer.append(sum(numbers[i:i+window]))

    return answer

print(solution([4,1,5,0,-4,1,-10], 3))
print(solution([4,1,5,0,-4,1,-10], 7))
print(solution([1,2,3,4,5], 2))