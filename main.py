import pandas as pd
import requests
from github import Github

token = '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'
g = Github(token)
headers = {'Authorization': 'token ' + token}


def get_wf(repo_full_name):
    return requests.get(f"https://api.github.com/repos/{repo_full_name}/actions/workflows", headers=headers).json()


rows = list()
repos = g.search_repositories(query='language:Java')

for i, repo in enumerate(repos):
    limit = g.get_rate_limit().core.remaining
    wf = get_wf(repo.full_name)
    if wf and int(wf['total_count']) > 0:
        rows.append({

            'url': f'https://github.com/{repo.full_name}',
        })
        print(rows)
df = pd.DataFrame(rows)
df.to_csv('repos.csv', index=False)
