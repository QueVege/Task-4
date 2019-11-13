import threading
from time import time


def fact(n):

    res = 1
    for i in range(n):
        res *= i + 1
    return res


if __name__ == "__main__":

    numbs = [3, 5, 7]

    threads = list()

    start = time()

    for n in numbs:
        t = threading.Thread(target=fact, args=(n,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time()

    print(f"Затраченное время: {end-start}")
