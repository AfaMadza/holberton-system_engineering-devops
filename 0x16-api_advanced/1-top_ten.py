#!/usr/bin/python3
'''
This module contains a script that queries an API
'''
import requests


def top_ten(subreddit):
    """
    Returns the top ten hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Agent007'}
    resp = requests.get(url, headers=header)
    try:
        info = resp.json().get('data').get('children')
        for child in range(10):
            post = info[child].get('data')
            title = post.get('title')
            print('{}'.format(title))
    except:
        print('None')
