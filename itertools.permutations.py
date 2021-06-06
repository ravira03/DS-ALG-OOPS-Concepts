from itertools import permutations
s,k = input().split(" ")

k = int(k)

permutations = list(permutations(s,k))
permutations.sort()

for i in permutations:
    print("".join(i))