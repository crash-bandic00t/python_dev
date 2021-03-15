import time


start = time.perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 11]
result = set()
tmp = set()

for i in src:
    if i not in tmp:
        result.add(i)
    else:
        result.discard(i)
    tmp.add(i)

# print(perf_counter() - start)
result_ord = [i for i in src if i in result]
print(result_ord)
print(time.perf_counter() - start)