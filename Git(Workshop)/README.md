
<img src="/pics/Docker.png">

## ▪️ Git & GitHub 🐈‍⬛

**Git and GitHub in a Nutshell:**

Basically a Version Control tool that will save your Dev life.
Git is used for local Version Control while Github is used to store remotely the changes.
You can have multiple branches to track changes and GitHub also offers interesting tools such as GitHub Actions.
To follow this sort of Tutorial-SnippetsList you'll need to make sure you have a Github account and git installed locally on your pc.
(Git should be already installed on your pc)

Install Git at [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), then verify your installation:

**OPTIONAL**

    > $ sudo apt-get update && sudo apt-get upgrade -y
    > $ sudo apt-get install git

Then, verify: 

	> $ git -v

Now, before moving on and getting started, you'd need to setup the authentication on your local machine for pushing (saving remotely) your changes to Github.
<br>
To do so, you have 2 ways:

**Auth Method 1:**

The First method for authentication to a remote GitHub Repository, is getting prompted for username and password everytime you want to push or pull from GitHub.
<br>
However, the password is not the GitHub account password, but rather a Personal Access Token, that you need to generate on GitHub and then store it safely somewhere on a block notes.
<br>
To generate the token, get into your account, then under settings, click on "Developer Settings".
<br>
From there, click on "personal access token" and then on "token (classic)".
<br>
Now, generate your token with the necessary permissions and store it somwhere safely.
<br>
Personally it's a bit silly and time consuming to type the Username and Token everytime I'd like to make some changes to a GitHub Repo, but it's my favourite approach as it gives me time to double think the push. 

**Auth Method 2:**
This authentication is a bit more time consuming at first, but then it will work like a charm every other time, and git won't ask you the username and password for pushes to a remote branch.
<br>
To do this, you'd need to add an ssh key on GitHub.
<br>
To generate an ssh key and add it to your ssh agent and then add to github, you might want to follow this 2 Tutorials from GitHub.

[Generate SSH Key and add to SSH agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

[Add SSH Key to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

<br>
Now, before moving on, we need to make sure that our repo is not using the http method for authenticating, otherwise it will ask us for username and password(token).
<br>
To check if your repository is using SSH or HTTPS by running git remote -v in your repository directory, AFTER you've added the remote repo to your local git repository.
<br>
This command will list the remote URLs for fetch and push operations. 
<br>
If the URLs start with https://, it means your repository is configured to use HTTPS 1, and so you need to change it to ssh method with

	> $ git remote set-url origin git@github.com:username/repository.git

If you'd like to further Troubleshoot any ssh Connections problems, checkout the TroubleshootSSH.md file in this repo.

**NOTE:** This method only work for the current directory, if you create a new one, you'll have to change the authentication method to ssh again.

### Workshop

Now, let's get Started with our Git and Github Workshop.
<br>
If, before starting, you simply want to clone (not synch and not having git to track the directory) a GitHub remote repo, you can do so with:

   > $ https://github.com/USERNAME/NAMEOFGITHUBREPO.git

<br>
First thing first, you'd need to create a local Repository and initialize git to track changes.

To do so:

   > $ mkdir GitWorkshop
   > $ cd GitWorkshop
   > $ git init

Now, if you'd like to synch with a remote GitHub Repo, simply create a new Repository on GitHub, and then follow the instruction on screen, which are:

   > $ git remote add origin https://github.com/YOURUSERNAME/NAMEOFGITHUBREPO.git
   > $ git branch -M main

Where the -M flag stands for "Master Branch", so you're naming your master branch as main.
<br>
This way you have synched your remote github repo with your local one and you've created the branch "main", whose name is quite self-explainatory.
<br>
To save our current progress in git and to commit (confirm) the changes made and eventually push them to the remote repository, we need to:

   > $ git add .

To add all the files (now changed) to add the changes to the staging area.

   > $ git commit -m "your very important commit message here"

To confirm all the changes in our staging area.

   > $ git push -u origin main

To eventually push the changes to the remote repository on github, where with the flag -u Git not only pushes your changes to the remote repository but also sets the upstream (tracking) reference for the current branch, so in case you are pushing or pulling without specifying the branch (NOT RECOMMENDED), git will know to wich branch pull or push to.
also 
<br>
If you would like to check all the changes you've made before committing them, you can check them with:

   > $ git status

If you'd like to see all the commits made, you can with:

   > $ git log

In order to push changes to a remote repo, you need to make sure that all changes are synched, in fact, if someone else changes the content of the repo, you'd need to pull the latest changes to be able to push them.
<br>
Also, when you want to clone a repository but having that synched with a local git repo, so after you've made some changes you want to push them, you'd need to pull the changes as well.

   > $ git pull origin branchname

Now, say that you want to modify your code, but not touch the main branch.
<br>
In order to create a new branch to commit and push some changes to, you have to:

   > $ git checkout -b newbranchname

This order will create a new branch and immediately switch to it.
<br>
Then you can make all the changes you want and add-commit-push the changes to your remote repo.
<br>
Now that you've made some changes, you're more likely to be willing to merge them.
To do that, git checkout in your desired branch and git merge the branch you'd like to fetch the changes from.

   > $ git checkout branchname
   > $ git merge anotherbranch.

This will merge the differences in anotherbranch to branchname.
<br>
Mind that merge won't delete files that are not present in the second branch.
<br>
Now, say that you are assigned to work on a project, started some time ago, and to work on a specific branch.
<br>
To achieve that, you'd need to:

   > $ mkdir newdir
   > $ cd newdir
   > $ git init
   > $ git remote add origin https://github.com/USERNAME/NAMEOFGITHUBREPO.git
   > $ git checkout -b branchname 
   > $ git pull origin branchname

Were git pull origin branchname drwas all the changes from the remote repo.
<br>
Obviously the branchname are all the same, and make sure the branch exists in your local repo with git checkout -b newbranchname.
<br>
Then, after you've made some changes:

   > $ git add . 
   > $ git commit -m "super important commit message"
   > $ git push -u origin branchname

Now, in case you would like to undo something in Git and get back to a previous commit, you'd need to use git reset and then forcefully push into the remote repo, for example:

   > $ git reset --hard HEAD~1

   OR

   > $ git reset --soft HEAD~1

   THEN

   > $ git push -u --force origin branchname 

   OR

   > $ git push -u --force-with-lease origin branchname 

In git reset HEAD~1 refers to the previous commit than the last one, to go even further back, simply increase the number OR, place the commit ID that you can retrieve with git log.
<br>
Also, the difference between hard and soft flags is that soft leaves your working directory and staging area (index) unchanged. 
<br>
This means the changes from the undone commit will still be staged, ready for you to modify and commit again.
<br>
On the other hand, if you want to completely undo the last commit and discard all changes associated with it, you can use the --hard flag with git reset. 
<br>
This is a more drastic action and should be used with caution, as it permanently removes the commit and all changes associated with it.
<br>
Use --force-with-lease for safer force pushing: The --force-with-lease option is a safer alternative to --force. 
<br>
It will only force push if the remote branch is at the state you expect, preventing you from accidentally overwriting someone else's work.

### Some other useful commands:

To delete a branch:

   > $ git branch -d branchname

To list only local branches:

   > $ git branch

To list both local and remote branches:

   > $ git branch -a

To show the changes between commits:

   > $ git diff

To Fetch changes from the remote repository without merging.

   > $ git fetch

**OPTIONAL:**

.gitignore
<br>
In case you want to add all the files with git add . but need to exclude some files or even some folders, you can write down a .gitgnore file in your directory, containing the name of the files to be ignored.
<br>
To ignore a file:

	filename OR foldername/filename OR foldername/* with * operator for "ALL FILES"

To ignore a folder:

	foldername/

NOTE that .git doesn't need to be added to .gitignore, since it's "ignored" by default, although it's the folder that makes things working. 
<br>
If you would like to delete a LOCAL branch:

	> $ git checkout main
	> $ git branch -d branchtodelete

This will change branch and delete the different branch you wanted to delete, you can also use the -D flag to force delete instead of -d soft delete.
<br>
If you would like to delete a REMOTE branch:

	> $ git push origin --delete branchtodelete

Where you can also use the -d shorthand flag or -D to force deletion.
<br>
If for some cases you would like to create a new empty branch (since branches always "clone" the main branch as starting point)

	> $ git switch --orphan newbranchname (RECCOMENDED for Git v2.23+)
	OR
	> $ git checkout --orphan newbranchname

Then, check that the tracking of that branch is truly empty with:
	
	> $ git rm -rf .

Finally, to push this new branch to a remote repository, you need to make at least one commit, even if it's an empty commit:

	> $ git commit --allow-empty -m "Initial commit on new branch"
	> $ git push -u origin newbranchname

AGAIN, FOR THE SAKE OF REPETITION: to create a new branch, with the master branch cloned on it:

	> $ git checkout -b newbranchname		<--- Creates Branch and Switches to it
	> $ git branch newbranchname			<--- Simply Creates Branch
	> $ git branch newbranchname branchtoclone 	<--- Simply Creates Branch and Clones as Starting point another onw specified rather than main (Master Branch)
	> $ git checkout branchname			<--- Simply Switches to Branch

To see which branch is being tracked:

	> $ git branch		<--- the tracked branch will appear green written and with a * preceding the branch name

*OPTIONAL:*
*CASE 1:*
Say that you want a different empty folder to only track and push to a brand new empty branch of your remote repository.
<br>
In that case, you'll need to:

	> $ mkdir newemptyfolder
	> $ cd newemptyfolder
	> $ git init
	> $ git checkout -b brandnewbranch
	> $ git remote add origin https://github.com/USERNAME/NAMEOFGITHUBREPO.git
	> $ touch test.txt	<--- Just a random test file to push something not empty to the new branch		
	> $ git add --all
	> $ git commit -m "Testing Commit from Empty Folder"
	> $ git push -u origin brandnewbranch

*CASE 2:*
Say that you have been assigned to actually only on an experimental new feature on a different branch named "devbranch" on the Repository, so you won't have access or push any changes to other branches, but only focus on that one.
<br>
In that case, you'll need to:
	
	> $ mkdir newemptyfolder	<--- NOT NECESSARY SINCE WHEN CLONING IT CREATES A FOLDER WITH THE NAME OF THE REPO
	> $ cd newemptyfolder		<--- NOT NECESSARY SINCE WHEN CLONING IT CREATES A FOLDER WITH THE NAME OF THE REPO
	> $ git clone -b devbranch --single-branch https://github.com/USERNAME/NAMEOFGITHUBREPO.git
	> $ cd folderwithreponame	
	> $ git checkout devbranch	<--- NOT with the -b flag as the branch already exists, make sure you get the name correctly.
	> $ git branch			<--- Make sure you only have the desired branch and it's the only one
	> $ git pull origin devbranch   <--- In case there have been recent pushes and you need to get those changes
	> $ git branch --set-upstream-to=origin/devbranch devbranch	<--- OPTIONAL, just sets the upstream to remoterepo/devbranch to our local devbranch
	> $ touch testfrommyfolder.txt	<--- OPTIONAL, just making sure
	> $ git add --all
	> $ git commit -m "Hey there pushing from my local repo on that specific branch"
	> $ git push -u origin devbranch	<--- Pushing changes to that specific branch we've been assigned to, the -u flag for setting the upstream is optional.

*OPTIONAL:*
If you are as lazy as me and want to only insert your Username and GitHub authentication token once and you want your system to store them for future usage, then:

	> $ git config --global credential.helper 'cache --timeout=3600'	<--- One hour (3600 are seconds) credentials cached
	> $ git config --global credential.helper store		<--- Stored forever even after rebooting

If you decide later that you want to remove these stored credentials, you can do so by deleting the credential file located at ~/.git-credentials

*NOTE:*
You can configure custom credentials managers to work with git.

<br>
THIS IS NOT A COMPLETE LIST OF EVERYTHING GIT CAN DO, however it's a solid base to get you started.
<br>
You may as want get to know other commands such as rebase and cherry-pick, but for the sake of summarizing, I won't write them down here to keep this README short.
<br>
Some useful links:

[GitHub](https://github.com/)
[Git](https://git-scm.com/)
[Git Docs](https://git-scm.com/doc)
[GitHub Docs](https://docs.github.com/en)
[Complete list of Git Commands](https://git-scm.com/docs/git#_git_commands)