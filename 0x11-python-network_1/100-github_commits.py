#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""
import sys
import requests


def list_recent_commits(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"

    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad responses

        commits = r.json()
        for i in range(min(10, len(commits))):
            commit_info = commits[i]
            sha = commit_info.get("sha")
            author_name = commit_info.get("commit").get("author").get("name")
            commit_message = commit_info.get("commit").get("message")
            commit_date = commit_info.get("commit").get("author").get("date")

            print(f"Commit {i + 1}:")
            print(f"SHA: {sha}")
            print(f"Author: {author_name}")
            print(f"Message: {commit_message}")
            print(f"Date: {commit_date}")
            print("\n")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <repository>")
        sys.exit(1)

    username, repo = sys.argv[1], sys.argv[2]
    list_recent_commits(username, repo)
