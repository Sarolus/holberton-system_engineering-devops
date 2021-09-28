#!/usr/bin/python3
"""
    Queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers for a given
        subreddit.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    UserAgent = {"User-Agent": "ubuntu:test:v1.0 (by /u/kemitche)"}

    request = requests.get(url, headers=UserAgent)

    if request.status_code == 404:
        return 0

    return request.json().get("data").get("subscribers")
