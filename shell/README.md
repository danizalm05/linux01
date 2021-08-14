# shell
 Shell Scripting Tutorial
 
https://www.youtube.com/watch?v=hwrnmQumtPw
 
http://www.newthinktank.com/2016/06/shell-scripting-tutorial/


How commit a change to the README file.
 -------------------------------------------
 1: In your repository's list of files, click README.md.
 2: Above the file's content, click 'the pencil tag' 
 3: On the Edit file tab , type some information about yourself.

 4: Above the new content, click Preview changes.

 5: At the bottom of the page, type a short, meaningful commit message  	

 6: Below the commit message fields, decide whether to add your commit to the current branch or to a new branch. If your current branch is master, you should choose to create a new branch for your commit and then create a pull request.

 7:Click Propose file change.

 

 Git in local  computer
--------------------------------------
 1: In the  project dir run 'git  init'

  
2: Type  'git add .' to add all the files  .
3: Type  'git commit -m "Fix such and such"'
 


Push an existing repository
---------------

1: git remote add origin https://github.com/username/new_repo.git
2: git remote -v
3: git push -u origin master
      you need to print user name  and passward

if the next message appears:
     ! [rejected]        master -> master (non-fast-forward)
     error: failed to push some refs to 'https://github.com//username/new_repo'
     hint: Updates were rejected because the tip of your current branch is behind
     hint: its remote counterpart. Integrate the remote changes (e.g.
     hint: 'git pull ...') before pushing again.

you shold  run :
     git pull origin master   and after that run   git push -u origin master


changing  remote
------------------
 git remote set-url origin https://github.com/USERNAME/PRJECT_NAME.git

	 
dos commands	 
	 show hidden file in cmd  'dir /ah'
	 delete non empty dir  rmdir   /s  'dir name'
	 
Fork A Repo
-----------------



A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

Most commonly, forks are used to:
 1 Changes to someone else's project 
 2 Use someone else's project as a starting point for your own idea.

 
 
 
