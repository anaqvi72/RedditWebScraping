import pandas as pd
import requests
import dotenv

env = dotenv.dotenv_values()
client_ID = env['CLIENT_ID']
secret_Key = env['SECRET_KEY']

auth = requests.auth.HTTPBasicAuth(client_ID, secret_Key)
data = {
    'grant_type': env['GRANT_TYPE'],
    'username': env['USERNAME'],
    'password': env['PASSWORD']
}

headers = {'User-Agent': 'RedProject'}

res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']

headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

res = requests.get('https://oauth.reddit.com/user/alli782/saved?limit=1000', headers=headers)



def getRedData():
    df = pd.DataFrame()
    for post in res.json()['data']['children']:
        df = df.append({
            'title': post['data']['title'],
            'subreddit': post['data']['subreddit'],
            'score': post['data']['score']
        }, ignore_index=True)
    return df

