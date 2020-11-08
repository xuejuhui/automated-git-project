#!/bin/bash 


function create (){
    echo $(date)
    cd /c/WD/project
    python ~/ShellScripts/automated-git-project/createProject.py $1
    cd $1
    touch test.js
    echo "TEST A ";
}

"$@"