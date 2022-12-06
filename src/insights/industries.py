from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    csvfile = read(path)
    # industries = set()
    # for industry in csvfile:
    #     industries.add(industry['industry'])
    return {industry['industry'] for industry in csvfile}.difference({''})
# retorna {'Retail', 'Business Services', 'Non-Profit', 'Health Care' e mais


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_list = []
    for job in jobs:
        if job['industry'] == industry:
            industry_list.append(job)
    return industry_list
# retorno de exemplo = [
#     {'id': 1, 'industry': 'agriculture'},
#     {'id': 2, 'industry': 'agriculture'}
# ]
