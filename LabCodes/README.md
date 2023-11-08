# PythonLab2

# Git Basics

This guide will help you understand the basic Git commands for creating and managing pull requests and pushing your changes to a remote repository.

## Forking a Repository

1. Go to the repository you want to contribute to.
2. Click the "Fork" button <img width="105" alt="image" src="https://github.com/motassimkhan/PythonLab2/assets/68193240/d34b5917-25ee-4404-8f37-545d101b5e6a">
 in the upper right corner to create a copy of the repository in your own GitHub account.

## Cloning a Repository
To work on a local copy of the forked repository:

> git clone https://github.com/motassimkhan/PythonLab2.git
> cd PythonLab2 // here we are changing directory to the repo name
Creating a Branch

# Create a new branch for your changes:
> git checkout -b <branch-name> // this creates a new branch for example, 3086 will give "AymanUzayr-3086" branch name, make sure to give your rollNo.(3XXX).
Committing Changes
Commit your changes with a descriptive message:
> git add .
> git commit -m "Description of changes"

# Pushing Changes
Push your branch to your forked repository on GitHub:
> git push origin <branch-name>

# Creating a Pull Request
Go to your forked repository on GitHub.
Click on the "Pull Requests" tab.
Click the "New Pull Request" button.
Select the base repository and branch you want to merge your changes into.
Provide a descriptive title and comment explaining your changes.
Click "Create Pull Request."
Reviewing and Merging Pull Requests
Collaborators or project maintainers can review your pull request. Once approved:

Click the "Merge Pull Request" button.
Confirm the merge.
Your changes are now part of the base repository.
