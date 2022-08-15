from datetime import datetime
import shutil
import os
import argparse
from os.path import join, dirname
from typing import Tuple
from os import system

BASE_PATH = dirname(dirname(__file__))


def get_args_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument('--repository_url', help="""
    The Github repository URL of the microservice.
    """)

    return parser


def create_git_submodule(repository_url: str, repository_name: str, branch_name: str = 'main') -> Tuple[int]:
    # Reference:
    # https://stackoverflow.com/questions/1777854/how-can-i-specify-a-branch-tag-when-adding-a-git-submodule/18799234#18799234

    return tuple([system(command) for command in [
        # Creates the submodule
        f'git submodule add -b {branch_name} {repository_url}',
        # Updates it's content
        'git submodule update --remote',
        # Move to the submodule folder
        f'cd {repository_name}',
        # Creates the `main` branch if doesn't exists
        f'git checkout -b {branch_name} --track origin/{branch_name}',
        # If it does exist, reference it to track it's remote counterpart
        f'git branch -u origin/{branch_name} {branch_name}',
        # Move to the parent folder
        'cd ..',
        # Add the submodule repository configuration
        f'git add {repository_name}',
        # Commit the new changes, it's important not to push the changes yet.
        f'git commit -m "feat({repository_name}): Create submodule"',
        # And we can finally update the subdmoule, once again
        'git submodule update --remote',
        # Update the parent repo by pushing the changes
        'git push'
    ]])


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def update_changelog(repository_name: str) -> None:
    changelog_path = f'{join(BASE_PATH, repository_name)}/CHANGELOG.md'

    # Read in the file
    with open(changelog_path, 'r+') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(
        '[current_date]',
        datetime.now().strftime('%Y-%m-%d')
    )

    # Write the file out again
    with open(changelog_path, 'w+') as file:
        file.write(filedata)


def main() -> None:
    # Get the repository url
    parser = get_args_parser()
    repository_url: str = parser.parse_args().repository_url
    assert repository_url

    # Get the repository name and details
    repository_name = repository_url.split('/')[-1].split('.')[0]
    print(repository_url, repository_name)

    # Create the git submodule configuration
    submodule_conf_result = create_git_submodule(
        repository_url=repository_url,
        repository_name=repository_name
    )
    # print('Submodule configuration result', submodule_conf_result)

    # Copy the dummy content
    new_path = copytree(
        join(BASE_PATH, 'service-example'),
        join(BASE_PATH, repository_name),
    )
    # print('The new path', new_path)

    # Update the CHANGELOG's date
    update_changelog(repository_name=repository_name)

    # Create a new commit and push everything to the new repo
    system(' && '.join([
        f'cd {repository_name}/',
        'git add .',
        'git commit -m "chore: Initialize new babylon service"',
        'git push',
    ]))


if __name__ == '__main__':
    main()

# Example calls:
# - python ./tools/create-service.py --repository_url=https://github.com/jofaval/babylon-customers-service.git
# - python3 ./tools/create-service.py --repository_url=https://github.com/jofaval/babylon-customers-service.git
