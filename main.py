import requests as r
import json as j

url = 'https://api.github.com/users/Faddey32/repos'

response = r.get(url)
response_json = response.json()

for repo in response_json:
    print(f'Repo:{repo["name"]}, URL: {repo["html_url"]}')
