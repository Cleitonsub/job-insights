from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    csvfile = read(path)
    industries = set()
    for industry in csvfile:
        industries.add(industry['industry'])
    return industries.difference({''})
# retorna {'Retail', 'Business Services', 'Non-Profit', 'Health Care' e mais


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
