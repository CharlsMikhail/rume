#!/bin/bash

# Alias para git status
git config --global alias.s status

# Alias para git commit -m
git config --global alias.c 'commit -m'

# Alias para git checkout
git config --global alias.co checkout

# Alias para git branch
git config --global alias.br branch

# Alias para git log
git config --global alias.l 'log --oneline --graph --decorate'

# Alias para git add .
git config --global alias.a 'add .'

# Alias para git push
git config --global alias.p push

# Alias para git pull
git config --global alias.pl pull

# Alias para git diff
git config --global alias.d diff

# Alias para git reset
git config --global alias.r 'reset HEAD --'

# Alias para git merge
git config --global alias.m merge

# Alias para git stash
git config --global alias.st stash

# Alias para git fetch
git config --global alias.f fetch

# Alias para git remote
git config --global alias.rem remote

# Alias para git show
git config --global alias.sh show

# Alias para git status con detalles
git config --global alias.sd 'status -s'

echo "Alias de Git configurados exitosamente."
