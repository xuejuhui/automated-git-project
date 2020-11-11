#!/bin/bash 


function create (){
    echo $(date)
    cd /c/WD/project
    python ~/ShellScripts/automated-git-project/createProject.py $1
    cd $1
    touch README.md
    echo "# testing-pythonscript" >> README.md
    git add .
    git commit -m "first commit"
    git branch -M main

}

"$@"