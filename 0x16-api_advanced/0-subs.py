#!/usr/bin/python3
""" Get subscribers count from existing subreddit"""

import requests


def number_of_subscribers(subreddit):
    """ Request about.json to subredit"""
    DOMAIN = 'https://www.reddit.com/'
    USER_AGENT = 'linux:subredditscript:v1 (by /u/sancagar)'
    h = {'User-Agent': USER_AGENT}
    req = requests.get(DOMAIN + 'r/{}/about.json'.format(subreddit), headers=h)
    data = req.json().get('data')
    if data is None:
        return 0
    if data.get('subscribers') is None:
        return 0
    return(data.get('subscribers'))
