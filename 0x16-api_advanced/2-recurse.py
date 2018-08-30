#!/usr/bin/python3
'''
This module contains a script that queries an API
'''
import requests


def recurse(subreddit, hot_list=[], af=None):
    """
    Returns the list of all hot posts
    """
    try:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        params = {'after': af, 'count': str(len(hot_list)), 'limit': '100'}
        ua = {'User-Agent': 'Agent007'}
        resp = requests.get(url, headers=ua, params=params,
                            allow_redirects=False)
        info = resp.json().get('data')
        af = info.get('after')
        children = info.get('children')
        for child in children:
            post = child.get('data')
            title = post.get('title')
            hot_list.append(title)
        if af:
            return recurse(subreddit, hot_list, af)
        else:
            return hot_list
    except:
        pass
    return None
