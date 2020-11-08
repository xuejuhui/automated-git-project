# importing os module
import os
import sys
from github import Github
from dotenv import load_dotenv


load_dotenv()


github_access_token = os.getenv("github-access-token")


def mkdir():
    """
    docstring
    """
    folderName = str(sys.argv[1])
    cwd = os.getcwd()
    path = os.path.join(cwd, folderName)
    if os.path.exists(path):
        print(folderName + ' already exists')
    else:
        os.mkdir(path)
        print("Directory '% s' created" % folderName)
        print(path)


def access_github(access_token):
    """
    docstring
    """
    g = Github(access_token)
    for repo in g.get_user().get_repos():
        print(repo.name)


if __name__ == "__main__":
    # mkdir()
    access_github(github_access_token)
    print(github_access_token)
