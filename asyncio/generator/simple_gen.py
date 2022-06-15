from typing import Iterator, List


def fib(n: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)
    
    return numbers

print(fib(10))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fib() -> Iterator[int]:
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current

for n in fib():
    print(n, end = ', ')
    if n > 10000:
        break

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, %
