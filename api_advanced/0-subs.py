#!/usr/bin/python3
"""Function to return number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """DOC"""
    reddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    header = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url,
                            headers=header
                            )

    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    return 0