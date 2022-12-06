from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding='utf8') as csvfile:
        read_csvfile = csv.DictReader(csvfile)
        data_csvfile = []
        for data in read_csvfile:
            data_csvfile.append(data)
    return data_csvfile
# retorna todo o arquivo 'formatado' []


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    job_types = set()
    for job in jobs_list:
        job_types.add(job['job_type'])
    return job_types
# retorna {'OTHER', 'TEMPORARY', 'PART_TIME', 'FULL_TIME',
# 'CONTRACTOR', 'INTERN'}


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_types_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            job_types_list.append(job)
    return job_types_list
# retorno de exemplo = [
#       {'id': 1, 'job_type': 'PART_TIME'},
#       {'id': 2, 'job_type': 'PART_TIME'}
# ]
