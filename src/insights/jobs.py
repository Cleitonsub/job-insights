from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r", encoding="utf-8") as csvfile:
        read_csvfile = csv.DictReader(csvfile, delimiter=",", quotechar='"')
        # data_csvfile = []
        # for data in read_csvfile:
        #     data_csvfile.append(data)
        return [data for data in read_csvfile]  # list comprehension
# retorna todo o arquivo 'formatado' []


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    return [job['job_type'] for job in jobs_list]
# retorna {'OTHER', 'TEMPORARY', 'PART_TIME', 'FULL_TIME',
# 'CONTRACTOR', 'INTERN'}


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    # job_types_list = []
    # for job in jobs:
    #     if job['job_type'] == job_type:
    #         job_types_list.append(job)
    return [job for job in jobs if job['job_type'] == job_type]
# retorno de exemplo = [
#       {'id': 1, 'job_type': 'PART_TIME'},
#       {'id': 2, 'job_type': 'PART_TIME'}
# ]
