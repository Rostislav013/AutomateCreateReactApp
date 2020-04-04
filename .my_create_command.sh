#!/bin/bash

function create() {
    cd
    #source .env
    cd Documents/Projects
    npx create-react-app $1
    python /home/rostislav013/Documents/PythonProjects/automatenpx/create.py $1
    cd
    cd Documents/Projects/$1
    git init
    git remote add origin https://github.com/Rostislav013/$1.git
    git remote -v
    git add .
    git commit -m "Initial commit"
    git push origin master
    code .
    npm start
}
