from connect_git import connect
import subprocess

def get_repo():
    git = connect()
    user = git.get_user()
    repos = git.get_repos()
    return repos

if __name__ == '__main__':
    repos = get_repo()
    for repo in repos:
      if not subprocess.check_call(['git', 'clone', repo.clone_url]):
        pass
      else:
        print("Failed to clone the repository :(");
