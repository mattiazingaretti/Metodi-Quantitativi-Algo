import random

def k_smallest_elem(S, k):
    if len(S) == k == 1 :
        return S
    y = random.choice(tuple(S))
    S1 = {x for x in list(S) if x < y}
    S2 = {x for x in list(S) if x >= y}
    if k <= len(S1):
        return k_smallest_elem(S1, k)
    else:
        return k_smallest_elem(S2, k - len(S1))




#TESTING
S = {random.randint(1,1000) for i in range(20) }

k = random.randint(1,len(S))

print(S, k)
print(k_smallest_elem(S, k))

sortedSetToList = list(S)
sortedSetToList.sort()

print(sortedSetToList)
