#!/usr/bin/python3
"""
Function to return number of subscribers of a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: Number of subscribers if the request is successful, 0 otherwise.
    """
    reddit_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(reddit_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except requests.RequestException:
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit = "nonexistingsubreddit"
    print(number_of_subscribers(subreddit))
