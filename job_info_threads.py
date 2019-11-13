import threading
import requests
from time import time


def job_info(job, page_num):
    return requests.get("https://jobs.github.com/positions.json",
                        params={"description": job,
                                "page": page_num})


if __name__ == "__main__":

    jobs = ["Rails", "JavaScript", "Python"]
    pages = [1, 2]

    threads = list()

    start = time()

    for job in jobs:
        for page in pages:
            t = threading.Thread(target=job_info, args=(job, page))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    end = time()

    print(f"Затраченное время: {end-start}")
