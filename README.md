# X7_project  

<p><img align="left" width="260" height="100" src="https://assets.manchester.ac.uk/logos/hi-res/TAB_UNI_MAIN_logo/White_grounds/TAB_col_white_background.jpg">The team project of University of Manchester student: Alexandru Stoica, David Santoso, Diana Constantin, Ivan Zhechev, Long Hei Chiu, Sabreenderjit  Gurjit Singh and Ruyi Zhang. The project is a website where students from University of Manchester can donate items to other students who are in need of them.</p>

## Getting started
### Setting up 
After being added as a collaborator, if you haven't already, create an [SSH key](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) (or use an existing one) and [add it](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account) to your GitHub account. ([GitHub is moving away from account password authentication, so token- or SSH-based authentication is preferred.](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/)) If you have used HTTPS to clone the URL you can easily change to SSH with ```git remote set-url origin git@github.com:ijan1/X7_project.git```, otherwise just clone the repository in a folder with ```git clone git@github.com:ijan1/X7_project.git```. ```git clone``` implicitly adds *origin* as the remote, so if you wish to change it to something else you have to do so with ```git remote add <shortname> git@github.com:ijan1/X7_project.git```.

### Using git
#### Staging and commiting
- Stage files for a commit ```git add <file_name>```  
- Add message to the commit ```git commit -m <message>```
- Push the commit ```git push origin```

#### Branching
- To create a new branch you issue ```git branch <branch_name>```  
- To select the branch on which you want to work on ```git checkout <branch_name>```  
- To see if someone has pushed any changes ```git fetch origin```  
- To push to your branch ```git push origin <branch_name>```

#### Merging
To merge a new feature to your team's corresponding branch.

1. Stage and commit your changes.  
2. Make sure the **HEAD** is pointing to the correct receiving branch. Usually either ```frontend``` or ```backend```.  
2.1. If on the front-end team ```git checkout frontend```  
2.2. If on the back-end team ```git checkout backend```  
3. Fetch to make sure you are using the latest commit. ```git fetch origin```  
3.1. In case of a conflict, a new branch could be created to resolve the conflict before merging.
4. Pull the latest update. ```git pull origin```  
5. Merge the two branches ```git merge <branch_name>```

This will merge ```<branch_name>``` into another branch.

## Group conventions
- All new branches should follow the format of ```name/feature```  
- Commits should have descriptive/meaningful names, such as ```Implementation of feature A``` instead of ```bug fix```  
- ~~href="comp10140.html"  becomes  href="{% url 'comp10140'%}"~~
- Page nicknames should be included as a comment at the beginning of the file  
- Pages should have their filename as their nickname  
- The Project kanban board will be used to manage internal workflow and task assignment 

## Useful link for learning git
[Fetch vs Pull](https://www.git-tower.com/learn/git/faq/difference-between-git-fetch-git-pull/)  
[Git Fetch](https://www.atlassian.com/git/tutorials/syncing/git-fetch)  
[Git Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)  
[Git Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)  
[Git Advanced Merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging)  
!!!! [Interactive Git Branching tutorial](https://learngitbranching.js.org/) !!!!  
!!!! [Git cheatsheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf) !!!!  
!!!! [Git undo/In case of conflict](https://docs.gitlab.com/ee/topics/git/numerous_undo_possibilities_in_git/) !!!!
[Git Head](https://www.git-tower.com/learn/git/glossary/head)
