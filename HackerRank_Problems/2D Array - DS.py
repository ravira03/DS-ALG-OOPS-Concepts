def hourglassSum(arr, i, j):

    return sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])

arr = []

for itr in range(6):
    arr.append(list(map(int,input().rstrip().split())))

result = hourglassSum(arr,0,0)

for itr in range(4):
    for itr1 in range(4):
        result = max(result, hourglassSum(arr,itr,itr1))
print(result)
