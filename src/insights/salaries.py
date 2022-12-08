from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    csvfile = read(path)
    # salaries = set()
    # for salary in csvfile:
    #     if salary['max_salary'] != '' and salary['max_salary'].isdigit():
    #         salaries.add(int(salary['max_salary']))
    return max(
        int(salary['max_salary']) for salary in csvfile
        if salary['max_salary'] != '' and salary['max_salary'].isdigit()
    )
# test = get_max_salary("data/jobs.csv")
# print(test) # retorna 383416


def get_min_salary(path: str) -> int:
    csvfile = read(path)
    return min(
        int(salary['min_salary']) for salary in csvfile
        if salary['min_salary'] != '' and salary['min_salary'].isdigit()
    )
# test = get_min_salary("data/jobs.csv")
# print(test) # retorna 19857


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        'min_salary' not in job
        or 'max_salary' not in job
        or not str(job['min_salary']).isdigit()
        or not str(job['max_salary']).isdigit()
        or int(job['min_salary']) > int(job['max_salary'])
        or not str(salary).lstrip('-').isdigit()
    ):
        raise ValueError
    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])
# test = matches_salary_range({"max_salary": 10000, "min_salary": 200}, -1000)
# print(test)
# .lstrip('-') remove o '-' caso haja a esquerda do numero


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError as error:
            print(error)
    return jobs_list
