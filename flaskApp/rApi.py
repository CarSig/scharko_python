import requests
from auth import id, secret, username, password
import pandas as pd

auth = requests.auth.HTTPBasicAuth(id, secret)

data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}

headers = {'User-Agent': 'MyAPI/' + '0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
token = res.json()['access_token']
headers['Authorization'] =  f"bearer {token}"

me = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
hot = requests.get('https://oauth.reddit.com/r/python/hot', headers=headers)


df = pd.DataFrame()

for topic in hot.json()['data']['children']:
    df = df._append({
        'title': topic['data']['title'],
        'url': topic['data']['url'],
        'num_comments': topic['data']['num_comments'],
        'created': topic['data']['created'],
        'subreddit': topic['data']['subreddit']
    }, ignore_index=True)

print(df)

