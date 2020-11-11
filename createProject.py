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
    folder_name = str(sys.argv[1])
    cwd = os.getcwd()
    path = os.path.join(cwd, folder_name)
    if os.path.exists(path):
        print(folder_name + ' already exists')
    else:
        os.mkdir(path)
        print("Directory '% s' created" % folder_name)
        print(path)


def access_github(access_token):
    """
    docstring
    """
    folder_name = str(sys.argv[1])
    g = Github(access_token)
    repo = g.get_user().create_repo(folder_name)
    repo.create_file("/README.md", "init commit", 'readmeText')


if __name__ == "__main__":
    mkdir()
    access_github(github_access_token)
    print(github_access_token)
