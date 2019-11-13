from multiprocessing import Pool
from time import time


def fact(n):
    res = 1
    for i in range(n):
        res *= i + 1
    return res


if __name__ == "__main__":

    numbs = [3, 5, 7]

    pool = Pool(processes=len(numbs))

    start = time()

    for n in numbs:
        p = pool.apply_async(fact, [n])

    pool.close()
    pool.join()

    end = time()

    print(f"Затраченное время: {end-start}")
