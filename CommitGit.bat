
cls
git status
rem "Start  new   commit to github https://github.com/settings/tokens."
pause
git add .
git commit -m   %RANDOM%
pause 
cls

git push -u origin master
   pause
