from functools import reduce
def findCommon(L):
    def R(a, b, seen=set()):
        a.update(b & seen)
        seen.update(b)
        return a
    return reduce(R, map(set, L), set())

n = int(input())
list_of_lists = []
for i in range(0, n):
    list_of_lists.append(str(input()).split(" "))
result = findCommon(list_of_lists)
print(result)