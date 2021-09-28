#!/usr/bin/python3
"""
    Queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after="t3_"):
    """
        Returns a list containing the titles of all hot articles for
        a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit,
        after
    )
    UserAgent = {"User-Agent": "ubuntu:test:v1.0 (by /u/kemitche)"}

    request = requests.get(url, headers=UserAgent, allow_redirects=False)

    if request.status_code == 404:
        return None
    elif after is None:
        return
    else:
        for post in request.json().get("data").get("children"):
            hot_list.append(post.get("data").get("after"))
        after = request.json().get("data").get("after")
        recurse(subreddit, hot_list, after)
        return hot_list
