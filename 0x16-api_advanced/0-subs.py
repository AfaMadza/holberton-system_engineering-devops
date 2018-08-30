#!/usr/bin/python3
'''
This module contains a script that queries an API
'''
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Agent007'}
    resp = requests.get(url, headers=header)
    try:
        info = resp.json().get('data')
        subs = info.get('subscribers')
        return subs
    except:
        return 0
