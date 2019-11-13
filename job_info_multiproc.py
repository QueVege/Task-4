from multiprocessing import Pool
import requests
from time import time


def job_info(job, page_num):
    return requests.get('https://jobs.github.com/positions.json',
                        params={'description': job,
                                'page': page_num})


if __name__ == "__main__":

    jobs = ["Rails", "JavaScript", "Python"]
    pages = [1, 2]

    pool = Pool(processes=len(jobs)+len(pages))

    start = time()

    for job in jobs:
        for page in pages:
            p = pool.apply_async(job_info, [job, page])

    pool.close()
    pool.join()

    end = time()

    print(f"Затраченное время: {end-start}")
