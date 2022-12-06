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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
