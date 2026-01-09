def solution(change):
    count_500 = change // 500 # 1
    change = change - (count_500 * 500) # 888-500 = 388

    count_100 = change // 100 # 3
    change = change - (count_100 * 100) # 388-300 = 88

    count_50 = change // 50 # 1
    change = change - (count_50 * 50) # 88-50 = 38

    count_10 = change // 10 # 3
    change = change - (count_10 * 10) # 38-30 = 8

    count_5 = change // 5 # 1
    change = change - (count_5 * 5) # 8-5 = 3

    count_1 = change // 1 # 3

    return (count_500 + count_100 + count_50 + count_10 + count_5 + count_1)

print(solution(1370))
print(solution(888))
print(solution(100))