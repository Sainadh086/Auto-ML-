#!/bin/bash
conda deactivate
heroku login
heroku create varshan
git init
heroku git:remote -a varshan
git add .
git commit -m "Initial commit"
heroku addons:create heroku-postgresql:hobby-dev
heroku config -s | grep DATABASE_URL
heroku config:set DISABLE_COLLECTSTATIC=1
pushing project to deploy
git push heroku master
heroku run python3 manage.py migrate
heroku logs --tail

