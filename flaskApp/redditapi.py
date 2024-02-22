import requests
from auth import id, secret, username, password
import pandas as pd
from flask import Blueprint, render_template

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


# df = pd.DataFrame()

# for topic in hot.json()['data']['children']:
#     df = df._append({
#         'title': topic['data']['title'],
#         'url': topic['data']['url'],
#         'num_comments': topic['data']['num_comments'],
#         'created': topic['data']['created'],
#         'subreddit': topic['data']['subreddit']
#     }, ignore_index=True)





reddit = Blueprint('reddit', __name__)


@reddit.route('/test', methods=['GET' ])
def test():
    print('testing')
    return 'test'

@reddit.route('/reddit/<subreddit>', methods=['GET', 'POST'])
def reddit_view(subreddit):
    print('fetchin reddit data...')
    auth = requests.auth.HTTPBasicAuth(id, secret)

    data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }

    headers = {'User-Agent': 'MyAPI/' + '0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)
    token = res.json()['access_token']
    headers['Authorization'] = f"bearer {token}"

    me = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
    hot = requests.get(f'https://oauth.reddit.com/r/{subreddit}/hot', headers=headers)
    print(hot.json())

    subreddit =[]

    for topic in hot.json()['data']['children']:
        post = {
    'title': [topic['data']['title']],
    'url': [topic['data']['url']],
    'num_comments': [topic['data']['num_comments']],
    'created': [topic['data']['created']],
    'subreddit': [topic['data']['subreddit']]
}

        subreddit.append(post)
    print (subreddit)
    return render_template('reddit.html', subreddit=subreddit)

# def reddit():
#     return render_template('reddit.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

# @app.route('/reddit', methods=['GET', 'POST'])
# def reddit():
#     return render_template('reddit.html', tables=[df.to_html(classes='data')], titles=df.columns.values)2

   
# print(df)

