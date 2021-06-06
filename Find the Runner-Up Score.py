n = int(input())
arr = map(int,input().split())

highest = -101
secondHighest = -101

for num in arr:
    if num > secondHighest:
        if num > highest:
            secondHighest = highest
            highest = num
        elif num < highest:
            secondHighest = num
print(secondHighest)