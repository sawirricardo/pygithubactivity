import requests
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python hello.py <username>")
        return
    username = sys.argv[1]
    url = "https://api.github.com/users/{}/events".format(username)
    response = requests.get(url)
    if response.status_code == 200:
        for event in response.json():
            if event["type"] == "PushEvent":
                print("Pushed {} commits to {}".format(event["payload"]["size"], event["repo"]["name"]))
            elif event["type"] == "PullRequestEvent":
                print("Opened PR {} in {}".format(event["payload"]["number"], event["repo"]["name"]))
            elif event["type"] == "IssuesEvent":
                print("Opened issue {} in {}".format(event["payload"]["issue"]["number"], event["repo"]["name"]))
            elif event["type"] == "WatchEvent":
                print("Starred {}".format(event["repo"]["name"]))
    else:
        print("Error: {} ({})".format(response.json()['message'], response.status_code))


if __name__ == "__main__":
    main()
