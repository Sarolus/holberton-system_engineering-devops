#!/usr/bin/python3
"""
    Queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """
        Prints the titles of the first 10 hot posts for
        a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    UserAgent = {"User-Agent": "ubuntu:test:v1.0 (by /u/kemitche)"}

    request = requests.get(url, headers=UserAgent, allow_redirects=False)

    if request.status_code == 404:
        return "None"

    for post in request.json().get("data").get("children"):
        print(post.get("data").get("title"))
