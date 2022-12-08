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
        ('min_salary' or 'max_salary') not in job
        or type(job.get('min_salary')) is not int
        or type(job.get('max_salary')) is not int
        or job['min_salary'] > job['max_salary']
        or not str(salary).lstrip('-').isdigit()
    ):
        raise ValueError
    return job['min_salary'] <= int(salary) <= job['max_salary']
# test = matches_salary_range({"max_salary": 10000, "min_salary": 200}, -1000)
# print(test)
# .lstrip('-') remove o '-' caso haja a esquerda do numero


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
