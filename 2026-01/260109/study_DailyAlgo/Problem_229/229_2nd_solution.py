def solution(numbers):
    # 리스트를 집합으로 변환
    num_set = set(numbers)
    
    # 1부터 순차적으로 확인
    for i in range(1, len(numbers) + 2):
        # 집합에서 찾기 (O(1))
        if i not in num_set:
            return i
        
print(solution([1,2,3,4,6,7]))
print(solution([2,3,4]))
print(solution([1,2,3]))