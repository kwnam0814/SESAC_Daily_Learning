def solution(change):
    coins = [500, 100, 50, 10, 5, 1]
    count = 0

    for coin in coins:
        count += change // coin
        change = change % coin
    
    return count

print(solution(1370))
print(solution(888))
print(solution(100))