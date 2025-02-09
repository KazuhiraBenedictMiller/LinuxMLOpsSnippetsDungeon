
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

Now, you can configure your git as follows:

	> $ git config --global user.name "Your Name"
	> $ git config --global user.email "youremail@example.com"

Aliases can make Git commands shorter and easier to remember. For example, to shorten git status to gs:

	> $ git config --global alias.gs status

To view all your global configuration settings:

	> $ git config --global --list

Or to see all configurations including local and system levels:

	> $ git config --list

If you need to reset any configuration setting to its default:

	> $ git config --global --unset <setting>	<--- Replace <setting> with the name of the setting you want to reset.

Viewing Configuration Files
Git stores configurations in .gitconfig files located in different directories (~/.gitconfig for global settings, ~/.config/git/config, and .git/config within repositories for local settings). 
You can directly edit these files with a text editor if you prefer.

For a comprehensive list of all configurable options, refer to the official Git documentation or use man git-config command in your terminal.

	> $ man git-config

[Git Configurations](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)

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
To stage our current progress in git and to commit (confirm) the changes made and eventually push them to the remote repository, we need to:

   > $ git add .

To Undo a Git add --all:

	> $ git reset		<--- Unstage all Files
	> $ git reset HEAD <file>	<--- For Specific Files
	> $ git rm --cached <file>	<--- To clean cache

The git reset command itself does not remove files from your local folder; it primarily affects the staging area (index) and potentially the working directory, depending on the options used. Specifically:

git reset --hard: This command resets the index and working directory to match the HEAD commit. Any changes made to tracked files in the working directory since the last commit are discarded. However, it does not affect untracked files (new files that Git has not been told about). Untracked files remain untouched in your local folder 5.
git reset (without --hard): By default, git reset operates in "mixed" mode, which means it resets the index but not the working directory. Changes are kept in your working directory but are unstaged. Again, untracked files are unaffected 5.
To remove untracked files (those not previously staged or committed), you would use the git clean command. This command is specifically designed to remove untracked files from your working directory. Be cautious with git clean, as it permanently deletes these untracked files, making them unrecoverable unless you have backups elsewhere.

git clean -df: This command removes untracked files and directories. The -d option tells git clean to remove untracked directories in addition to untracked files, and -f stands for "force," which is required by default to confirm the potentially destructive action 13.
It's important to note that git clean is a powerful and potentially destructive command. Always double-check which files will be affected by running git clean -n (dry run) before executing the actual cleanup with git clean -df.

In summary, git reset affects the staging area and possibly the working directory but does not remove untracked files from your local folder. 
To remove untracked files, you would use git clean.

To add all the files (now changed) to add the changes to the staging area.

   > $ git commit -m "your very important commit message here"

If you want to actually open the commit file for a longer message simply go for:  
  
    > $ git commit

To confirm all the changes in our staging area.

   > $ git push -u origin main

To eventually push the changes to the remote repository on github, where with the flag -u Git not only pushes your changes to the remote repository but also sets the upstream (tracking) reference for the current branch, so in case you are pushing or pulling without specifying the branch (NOT RECOMMENDED), git will know to wich branch pull or push to.
also 
<br>
If you would like to check all the changes you've made before committing them, and eventually unstage some of them, you can check them with:

   > $ git status

If you've added changes to the staging area using git add and you are seeing them in git status, but decide you want to keep those changes in your working directory without them being considered for the next commit, you can use git restore to unstage those changes.

	> $ git restore --staged FILENAME.EXT

ALSO,
To unstage changes, you can simply use:

	> $ git restore <file>

To discard local changes, you can use:

	> $ git restore -- <file>

Advanced Options
--patch Option: This option allows you to interactively choose which changes to restore. It steps through each change and asks if you want to discard or keep it.
--staged Option: This option restores the file from the index (staging area) instead of the last committed state. It's useful if you've staged changes that you now want to unstage.
--worktree Option: When combined with --staged, this option restores both the staging area and the working tree to match the specified source. By default, the source is HEAD.
--source Option: Allows you to specify a different commit to restore from. This is useful if you want to revert changes to a specific earlier state.

Examples

To unstage changes for a specific file:

	> $ git restore --staged myfile.txt

To discard local changes for a specific file:
	
	> $ > $ git restore -- myfile.txt

To interactively choose which changes to restore:
	
	> $ git restore -p myfile.txt

To restore a file from a specific commit:

	> $ git restore --source=abc123 -- myfile.txt

Differences from Other Commands
Unlike git reset, which moves the current branch pointer, git restore does not alter the commit history. It only affects the working directory and/or staging area.
git restore is more focused on file-level changes, whereas git revert creates a new commit that undoes the changes made by other commits.

If you'd like to see all the commits made, you can with:

   > $ git log		<--- git log --oneline optional flag (there are more like --stat flag and --pretty=format, check the docs)

Then, to inspect a commit:

	> $ git show COMMITID	<--- Commit ID is the has of the commit in this format 1eab9bed33a4735a2cf16c61e86a207f3f499f80

You can also export it in a file with > filepath/filename.txt following the command.

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
In case you want to undo a Merge:

After merging a branch into another (usualy main or master branch), the branch remains in the repository unless explicitly deleted. 
There's no automatic deletion mechanism triggered by a merge operation.

Deleting a Merged Branch

If you decide to delete a branch after merging it, you can do so using the following command:

	> $ git branch -d <branch-name>

This command attempts to delete the specified branch. 
The -d option ensures that Git will prevent deletion if the branch has not been fully merged. 
If you're certain you want to delete the branch regardless of its merge status, you can force deletion with:

	> $ git branch -D <branch-name>

Undoing a Git Merge

If you need to undo a merge, the method depends on whether the merge has been pushed to a remote repository.

Local Repository Only: 
If the merge hasn't been pushed, you can use git reset to revert to the commit before the merge. 
For example, to go back to the commit just before the last one (assuming the merge was the most recent operation):
	> $ git reset --hard HEAD~1

Or, if you want to preserve uncommitted changes:

	> $ git reset --merge HEAD~1

Remote Repository: 
If the merge has been pushed, it's safer to use git revert to create a new commit that undoes the merge. 
This avoids rewriting history on the remote repository:

	> $ git revert -m 1 <merge-commit-hash>

Here, <merge-commit-hash> is the hash of the merge commit you want to undo. 
The -m 1 option specifies that you want to keep the parent side of the merge (the branch you merged into).

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

   > $ git reset --hard HEAD~1		<--- HEAD~1 means, previous commit HEAD~x means x+1 (since the commit 0 is current commit) commits ago, or you can also use the commit id that you can inspect with git log

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
If for some reason there are files cached in git and you keep pushing them while you don't want to (this usually happens if you already pushed them first and then added to .gitignore) and you want to remove them from the cache, so the .gitignore is not going to allow pushes to the remote repo:

	Add foldername/* to .gitignore
	git rm --cached -r foldername/* 	<--- to clear the cached files and ensure they won't be pushed.
	Then commit and Push to the remote repo.

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

*OPTIONAL: DIFFERENCES BETWEEN GIT FETCH AND GIT PULL (AI GENERATED BUT ACCURATE)*

The primary difference between git fetch and git pull lies in how they update your local repository and working directory with changes from a remote repository.

*Git Fetch:*

Purpose: git fetch is used to download commits, files, and refs from a remote repository into your local repository. Fetching is what you do when you want to see what everybody else has been working on. It's the command that tells your remote repositories to send the latest version of everything they have that you don't.
Effect on Local Repository: When you execute git fetch, Git retrieves the updates made to the remote repository (commits, branches, etc.) and stores them in your local repository under special references. These updates are not merged into your current branch or reflected in your working directory. This allows you to review the changes before deciding what to merge locally.

Use Case: Fetching is useful when you want to review recent changes to the project, compare them with your local work, or prepare for a merge. It's a safe way to bring your repository up to date without altering your working directory.

*Git Pull:*

Purpose: git pull is essentially a combination of git fetch followed by git merge. When you execute git pull, Git will fetch the branch from the remote repository and immediately attempt to merge it into the current active branch in your local repository.
Effect on Local Repository: Unlike git fetch, git pull updates both your local repository and your working directory. It merges changes fetched from the remote repository into your current branch, potentially modifying files in your working directory.

Use Case: Pulling is typically used when you're ready to update your local branch with the latest changes from the remote repository and merge them into your work. It's a convenient way to synchronize your local repository with the remote, especially when you're working alone or when you're confident that the merge will not result in conflicts.

*Summary:*

Safety and Control: git fetch offers more safety and control over the update process because it allows you to review changes before integrating them into your local branches. This makes it ideal for collaborative environments where understanding changes before merging is crucial.

Convenience: git pull is more convenient for quickly updating your branch with remote changes, especially in scenarios where merge conflicts are unlikely or easily resolved. It combines fetching and merging into a single step.

*EXTRA:*
Restoring to a specific commit in Detached Mode:

Using `git checkout <commit-hash>` allows you to navigate to a specific commit in your Git repository's history. 
Each commit in Git is identified by a unique alphanumeric string known as the commit hash. 
This hash serves as a reference point to the state of the repository at the time of that commit.

When you execute `git checkout <commit-hash>`, Git updates your working directory to reflect the repository's state at that specific commit. 
This means all files in your working directory will match how they were at the moment of the specified commit. 
This action is particularly useful for inspecting the project at various stages of development, testing older versions of the project, or reverting changes made after the commit.

It's important to note that checking out a commit places you in a "detached HEAD" state. 
In this state, you're not on any branch, meaning any new commits you make won't belong to any branch and could be lost unless you explicitly create a new branch while in this detached state or move back to an existing branch.
To return to working on a branch after checking out a commit, you simply use `git checkout <branch-name>`, replacing `<branch-name>` with the name of the branch you wish to return to, such as `main` or `dev`.

Here's a practical example:

1. To find the commit hash you want to checkout, you can use `git log`, which displays the repository's commit history along with the hashes.
2. Once you have identified the commit hash, execute `git checkout <commit-hash>` to navigate to that commit. For example, if the commit hash is `a1b2c3d`, you would run:
  
   > $ git checkout a1b2c3d
  
3. Your working directory now reflects the state of the project at commit `a1b2c3d`.
4. To return to working on a branch, say `main`, you would then run:
 
   > $ git checkout main
  
Now you are at the starting point before doing the git chechout with the commit-hash-id and you safely saw all changes.
Remember, while in the detached HEAD state, it's advisable to avoid making new commits unless you plan to create a new branch from this state to preserve those changes, or you'll overwrite commits after the hash-id one.

<br>
THIS IS NOT A COMPLETE LIST OF EVERYTHING GIT CAN DO, however it's a solid base to get you started.
<br>
You may as want get to know other commands such as rebase and cherry-pick that are incredibly helpful (and i suggest to check out the docs and play around with them, but for the sake of summarizing, I won't write them down here to keep this README short.
<br>
Also, I think that the best way to play around and get experienced with git is to create a local repo, synch it with a remote one and then experiment all commands and possible scenarios, just like a workshop, with hands-on, then write down what you did.

Some useful links:

[GitHub](https://github.com/)
[Git](https://git-scm.com/)
[Git Docs](https://git-scm.com/doc)
[GitHub Docs](https://docs.github.com/en)
[Complete list of Git Commands](https://git-scm.com/docs/git#_git_commands)


*MY FAVOURITE GIT STRATEGY:*

Github (Git) Strategy:

In the sea of Git Strategies for every kind of Software Engeneering, where you can either use them as they were initially studied or also take inspiration from some of them and use creativity to solve Development Collaboration Challenges, my most Favourite by far is the GitHub (Git) Strategy.

"Visual" Explanation:
			
					       Production																		   Production
Main Branch ───┬───────────────────────────────────────────────────────────────────────┬─── Pull Request from Dev Branch to Merge Changes ─── Lots of Testing ───┬──────────────────────────────────────────────────────────────────────────────────────────┬─── Pull Request from Dev Branch to Merge Changes ─── Lots of Testing ───>
	       │								       │							                 │											    │
	       │								Lots of Testing						                         │									             Lots of Testing
	       │								       │						                         │											    │
	       └── Dev Branch ─── New Changes ─── Good Changes Pushed to Dev Branch ───┘                                                                         └── Pull Request from Main Branch ─── New Changes ─── Good Changes Pushed to Dev Branch ───┘                          


Technical Explanation:

When Working on a new feature for your project, since you don't want to break production, you'll need to checkout on a new Dev Branch.
Usually this Dev Branch is being kept and reused for future features.
On the Dev Branch, you'll start developing the new changes and committing them Locally.
Then, if you're happy with the result you've obtained, you'll push the Changes to the Remote Repo Dev Branch, that to this point, is only synched with the Production Branch, so in practice, until now, on the Remote GitHub Repo Production Branch and Dev Branch have the same exact code.
However, when you're Pushing local changes to the Dev Branch, you'll need either GitHub Actions or any other Cron-Like Jobs that will run many different kind of tests on the new code pushed to the Branch.
At this stage when Pushing you'll only need to Run Unit and Integration type of tests to Ensure Code Integrity.
Then, since you want to keep the Dev Branch for future Development of new Features, you need to open a Pull Requests on the Main Branch to Fetch Code Changes and there, you'll need to run Perfomance tests and Metrics type of Tests.
All the Testing is obviously triggered by an automated Cron-Like Tool.
Then, the GitHub Action, will either reject the Pull Request if the changes have poor metrics, or implement in prouction.

Practical Explanation:

You have a Production Environment on your main branch, but the data skewed a bit since the last time you trained a machine learning model and Metrics are getting worse.
You'll create a Dev Branch, work a bit on your code locally and see if you can make up a better model.
If changes are satisfying, you'll push those changes to the Remote Repo Dev Branch, where a GitHub Action will get triggered and run Integration and Unit Tests.
From There, when you are ready to push those changes to Production, you'll need to open a Pull Request (can be automated as well if code passes Unit and Integration Testing) from your Main Branch.
On that Pull Request, the GitHub Action on the main branch will get Triggered, running the code before it reaches the Production Environment whilist it's staged and then it will run some other Testing, usually an End-to-End Testing.
Lastly, if the new model that will be trained with the code Pulled to the Main Branch is better than the production model, you accept the changes, otherwise, reject the Pull Request.   

Pros:
- Very Modular and Scalable
- It shines with small teams and operations but works like a charm for bigger ones
- Ensure Integrity without compromising Interpretability and Explainability

Cons: 
- Lots of Testing and DevOps (Cloudly Triggered for the most) on your end (not really a con, but it's extra work anyways)
- Neckbeards will look down on you, reminding you that you should never use an IDE, but rather a text editor, also: you still not using Arch btw? All that Debian does is being Stable, it's a Boomer Distro.

Technical Insights:

Branch Management: Emphasize the importance of keeping the Dev Branch clean and up-to-date with the Main Branch through regular merges or rebases. 
This ensures that feature development starts from the most recent stable base, minimizing merge conflicts and integration issues.

Testing Stages: Clarify the distinction between initial testing on the Dev Branch (focusing on code correctness and integration) and subsequent testing during the pull request phase (evaluating performance, security, and end-to-end functionality). 
Highlighting these stages helps in understanding the comprehensive testing strategy employed.

Most common type of Testing:

Unit Testing: Focuses on testing individual components, methods, or functions of the software in isolation. 
It's designed to validate that each unit of the software performs as expected. 
Unit tests are typically written and executed by software developers and are known for their speed and ease of automation.

Integration Testing: Verifies the interaction between different parts of the software to ensure they work together as intended. 
This type of testing is crucial for identifying issues that arise when components are combined, such as communication problems or data inconsistencies. 
Integration testing follows unit testing in the software development lifecycle and precedes system testing.

Functional Testing: Also known as black-box testing, it focuses on testing the software's functionality against the requirements/specifications. 
Functional tests validate that the software behaves as expected under various conditions and inputs, without considering the internal workings of the software.

Acceptance Testing: Performed to determine whether a system meets the specified criteria for acceptance. Acceptance testing can be further divided into two types:
	User Acceptance Testing (UAT): Conducted with actual users to ensure the system meets their needs and expectations.
	Business Acceptance Testing (BAT): Focuses on meeting business requirements and processes.

System Testing: Involves testing the entire system as a whole to ensure it meets the specified requirements. 
This type of testing validates the integration of all components and checks the system's compliance with the defined specifications.

End-to-End Testing: Validates the flow of an application from start to finish. 
It tests the entire workflow of an application in a real-world scenario, including communication with databases, networks, other systems, etc., to ensure the integrated components function together as expected.

*GIT PULL VS MERGE VS FETCH VS REBASE:*

The primary difference between git pull and git merge lies in their operation and automation levels:

Operation:
git merge operates locally within your repository, merging changes from one branch into another within the local environment.
git pull, on the other hand, involves both local and remote operations. It fetches changes from a remote repository and then merges them into the local branch.
Level of Automation:
git merge requires manual specification of the branch you wish to merge, offering more control over the merging process.
git pull automates the process of fetching and merging changes from a remote repository, providing convenience but less control over the specifics of the merge.
Key Points to Consider
Understanding Their Roles: Knowing when to use git pull versus git merge is crucial for effective version control management. git merge is ideal for integrating changes between local branches, offering precise control. Conversely, git pull is beneficial for incorporating remote changes into your local branch, simplifying collaboration but with reduced control over the merge details.
Automation and Control: While git pull automates fetching and merging, potentially speeding up workflows, it may not always align with the desired level of control, especially in complex projects. git merge allows for a more deliberate approach, enabling developers to review and adjust merges as needed.
Use Cases:
Use git merge when you need to integrate changes from one local branch into another, particularly when you want to carefully manage how the histories of these branches are combined.
Opt for git pull when you're looking to update your local branch with the latest changes from a remote repository, prioritizing convenience and efficiency in fetching and merging those changes.
Conclusion
Choosing between git pull and git merge depends on your specific workflow needs and the level of control you desire over the merging process. git merge offers more granular control for local branch integrations, while git pull provides a streamlined method for incorporating remote changes. Understanding these differences is essential for leveraging Git's capabilities effectively in project management and collaboration scenarios.


git fetch and git pull are both Git commands used to interact with remote repositories, but they serve different purposes:

git fetch retrieves updates from the remote repository but does not apply any changes to your local repository. It allows you to view the changes made in the remote repository without affecting your local work. After fetching, you can decide whether to merge the changes into your local branch manually using git merge.
git pull, on the other hand, is essentially a combination of git fetch followed by git merge. When you execute git pull, Git automatically fetches the updates from the remote repository and attempts to merge them into your current local branch. This means that git pull modifies your local repository by applying the fetched changes immediately.
Key Points to Consider
Purpose and Behavior:
Use git fetch when you want to see what changes have been made to the remote repository without altering your local workspace. This is useful for reviewing changes before deciding to incorporate them.
Use git pull when you are ready to update your local branch with the latest changes from the remote repository, understanding that this action will merge those changes into your current branch.
Control Over Merging:
git fetch gives you full control over when and how to merge changes into your local branches. This is beneficial when you need to review changes or resolve potential conflicts manually.
git pull automates the fetching and merging process, which can be convenient but reduces your ability to review changes before they are integrated into your local branch.
Workflow Integration:
Integrating git fetch into your workflow allows for a more cautious approach to managing remote changes, especially in collaborative environments where careful consideration of changes is necessary.
git pull is suitable for straightforward updates where immediate integration of remote changes is desired, and there's confidence that the merge will not introduce significant conflicts.
Conclusion
Choosing between git fetch and git pull depends on your specific needs regarding control over the merging process and how you prefer to handle updates from remote repositories. git fetch offers a safer, more controlled way to review and selectively merge changes, while git pull provides a quicker, more automated method to stay up-to-date with remote changes. Understanding the differences and implications of these commands is crucial for effective Git usage in version control and collaboration scenarios.


Using git rebase instead of git merge when syncing changes from the Main Branch to the Dev Branch offers several advantages, primarily related to maintaining a cleaner and more linear commit history. Here's what happens during a rebase operation:

Rebasing moves or combines the commits of one branch onto another branch. When you perform a rebase, Git takes the changes made in the commits of the branch being rebased and replays them on top of the base branch. This process effectively "rewrites" the project history by creating new commits for each commit in the original branch.
Cleaner History: Unlike merging, which creates a new "merge commit" to reconcile the histories of the two branches, rebasing maintains a linear commit history. This can make the project history easier to follow and understand, as it avoids the complexity introduced by merge commits.
Conflict Resolution: During a rebase, conflicts may arise if the changes in the branch being rebased conflict with changes in the base branch. These conflicts must be resolved manually, commit by commit, as Git replays the changes. This can lead to a more thorough understanding of the conflicts and their resolutions compared to resolving a single large conflict during a merge operation.
Commit Rewriting: Rebasing allows for the rewriting of commit history, which can be both an advantage and a risk. On the positive side, it enables cleaning up a messy history before merging a feature branch into the mainline. However, it's important to note that rewriting history can be dangerous for shared branches, as it alters the existing commit history that others may have based their work upon.
Given these characteristics, using git rebase in the context of keeping the Dev Branch up-to-date with the Main Branch can ensure that the Dev Branch has a clean, linear history that reflects the latest changes from Main without unnecessary merge commits. This approach is particularly useful in collaborative environments where maintaining a clear and understandable project history is beneficial.


You said:
how do I synch a remote repository on github to a local one ??

here's the link

https://github.com/KazuhiraBenedictMiller/LinuxMLOpsSnippetsDungeon
ChatGPT said:
ChatGPT

To synchronize the remote GitHub repository LinuxMLOpsSnippetsDungeon with your local machine, follow these steps:

    Clone the Repository:

    If you haven't already cloned the repository, execute:

git clone https://github.com/KazuhiraBenedictMiller/LinuxMLOpsSnippetsDungeon.git

This command creates a local copy of the repository.

Navigate to the Repository Directory:

cd LinuxMLOpsSnippetsDungeon

Add the Remote Repository:

To link your local repository to the remote one, add it as a remote:

git remote add origin https://github.com/KazuhiraBenedictMiller/LinuxMLOpsSnippetsDungeon.git

This command sets the remote repository URL and names it origin.

Fetch Changes from the Remote Repository:

To retrieve updates from the remote repository without merging them into your local branch, use:

git fetch origin

This command downloads objects and refs from the remote repository.

Merge Changes into Your Local Branch:

To integrate the fetched changes into your local branch, execute:

git merge origin/main

This command merges the changes from the remote main branch into your current branch.

Push Local Changes to the Remote Repository:

If you've made changes locally and want to update the remote repository, use:

    git push origin main

    This command uploads your local commits to the remote repository's main branch.

By following these steps, you can effectively synchronize your local repository with the remote GitHub repository.
You said:
I got this problem:

git remote add origin https://github.com/KazuhiraBenedictMiller/LinuxMLOpsSnippetsDungeon.git
fatal: not a git repository (or any of the parent directories): .git
ChatGPT said:
ChatGPT

The error message fatal: not a git repository (or any of the parent directories): .git indicates that the current directory is not recognized as a Git repository. This typically occurs when you attempt to execute Git commands in a directory that hasn't been initialized as a Git repository.

To resolve this issue, follow these steps:

    Clone the Repository:

    If you haven't already cloned the repository, you can do so by running:

git clone https://github.com/KazuhiraBenedictMiller/LinuxMLOpsSnippetsDungeon.git

This command creates a local copy of the repository on your machine.

Navigate to the Cloned Repository:

After cloning, move into the repository's directory:

    cd LinuxMLOpsSnippetsDungeon

    Once inside this directory, you can execute Git commands without encountering the previous error.

By ensuring you're operating within the correct directory, Git will recognize the repository, and you'll be able to manage it as intended.
You said:
what if I have files already on my machine, I want to synch and fetch
ChatGPT said:
ChatGPT

To synchronize your existing local directory with the remote GitHub repository LinuxMLOpsSnippetsDungeon, follow these steps:

    Initialize the Local Directory as a Git Repository:

    Navigate to your local project directory:

cd /path/to/your/local/directory

Initialize the directory as a Git repository:

git init

Add the Remote Repository:

Add the remote repository and name it origin:

git remote add origin https://github.com/KazuhiraBenedictMiller/LinuxMLOpsSnippetsDungeon.git

Fetch the Remote Repository:

Retrieve the remote repository's data without merging:

git fetch origin

Set Up Tracking for the Remote Branch:

Create a local branch named main that tracks the remote main branch:

git checkout -b main --track origin/main

Merge Remote Changes into Your Local Repository:

Merge the fetched changes into your local repository:

git merge origin/main

If there are conflicts between your local files and the remote repository, Git will prompt you to resolve them. Open the conflicting files, make the necessary adjustments, and then mark them as resolved:

git add <resolved_file>

After resolving all conflicts, complete the merge:

git commit

Push Local Changes to the Remote Repository:

If you've made changes locally that you want to push to the remote repository, use:

    git push origin main

By following these steps, you can synchronize your existing local directory with the remote GitHub repository, ensuring both are up to date.
You said:
git creates my deafult branch as master how do i change that?
ChatGPT said:
ChatGPT

To change Git's default branch name from master to main, you can configure Git to use main for all new repositories you initialize. This ensures consistency across your projects and aligns with modern conventions. Here's how to do it:

    Set the Default Branch Name Globally:

    Open your terminal and execute the following command:

git config --global init.defaultBranch main

This command sets the default branch name to main for all new repositories you create using git init. The --global flag ensures this setting applies to all Git repositories on your system.
Stack Overflow

Rename the Default Branch in Existing Repositories:

For repositories that have already been initialized with master as the default branch, follow these steps to rename the branch to main:

    Rename the Local Branch:

    Navigate to your repository's directory and run:

git branch -m master main

This command renames the local master branch to main.

Update the Remote Repository:

Push the newly named main branch to the remote repository and set it as the upstream branch:

git push -u origin main

This command uploads the main branch to the remote repository and establishes tracking between your local and remote branches.

Change the Default Branch on the Remote:

On platforms like GitHub, navigate to your repository's settings and change the default branch to main. This step ensures that the remote repository recognizes main as the primary branch.
Hanselman.com

Delete the Old master Branch on the Remote:

After confirming that main is set as the default branch on the remote, delete the old master branch to prevent confusion:

        git push origin --delete master

By following these steps, you ensure that both new and existing repositories use main as the default branch, promoting consistency and adhering to current best practices.
You said:
how do i see the differences in files between my local repo and the remote one?
ChatGPT said:
ChatGPT

To compare the differences between your local repository and its remote counterpart, follow these steps:

    Fetch the Latest Changes from the Remote Repository:

    Before performing any comparisons, ensure your local repository has the latest information from the remote repository. This can be done using:

git fetch origin

This command retrieves updates from the remote repository without merging them into your local branches.

Compare Local and Remote Branches:

To view the differences between your local branch and its corresponding remote branch, use the git diff command:

git diff <local-branch> origin/<remote-branch>

For example, if you're working on the main branch:

git diff main origin/main

This will display the changes that exist in your local main branch compared to the remote main branch.

Compare Specific Files Between Local and Remote Branches:

If you're interested in the differences of a specific file between your local and remote branches, you can specify the file path:

git diff <local-branch>:<file-path> origin/<remote-branch>:<file-path>

For instance, to compare a file named example.py in the main branch:

    git diff main:example.py origin/main:example.py

By following these steps, you can effectively identify and review the differences between your local repository and the remote repository, allowing you to synchronize changes as needed.
You said:
how do I automatically set up my username and token for pushing without bothering about typing?
ChatGPT said:
ChatGPT

To avoid repeatedly entering your username and personal access token (PAT) when pushing to GitHub, you can configure Git to securely store your credentials. This can be achieved by using Git's credential helper, which caches or stores your credentials, allowing for seamless authentication. Here's how to set it up:

    Configure Git to Store Credentials:

    Open your terminal and execute the following command:

git config --global credential.helper store

This command tells Git to store your credentials in a plain text file on disk, enabling automatic authentication for future Git operations.
mgimond.github.io

Perform a Git Operation to Trigger Credential Storage:

After configuring the credential helper, perform a Git operation that requires authentication, such as pushing to your repository:

    git push https://github.com/your-username/your-repository.git

    During this operation, Git will prompt you for your username and PAT. Enter them as requested.

    Credentials Are Now Stored:

    Once you've entered your credentials, Git will store them in a file located at ~/.git-credentials. Future Git operations will use these stored credentials, eliminating the need for repeated authentication prompts.

Important Considerations:

    Security Implications: Storing credentials in plain text can pose security risks, especially if others have access to your system. Ensure that your system is secure and that you understand the implications of storing credentials in this manner.

    Alternative: Using SSH Keys: For enhanced security, consider using SSH keys for authentication. SSH keys provide a secure and convenient method of authenticating with GitHub without storing plain text credentials. You can generate an SSH key pair and add the public key to your GitHub account. Detailed instructions are available in GitHub's documentation.

By configuring Git to store your credentials or by setting up SSH keys, you can streamline your workflow and avoid the hassle of entering your username and PAT for every push operation.


To view the list of files tracked by Git in your repository, you can use the following commands:

1. List all tracked files in the current branch:

git ls-files

This command displays all files that are currently tracked by Git in your working directory. 


2. List all tracked files in the current branch, including those in subdirectories:

git ls-tree --full-tree --name-only -r HEAD

This command lists all files that are tracked and have been committed in the current branch, recursively including files in subdirectories. 


3. List all files that have ever been tracked, including deleted files:

git log --pretty=format: --name-only --diff-filter=A | sort - | sed '/^$/d'

This command provides a list of all files that have ever been added to the repository, including those that have been deleted. 



These commands can help you inspect the files managed by Git in your repository.