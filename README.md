# python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started

$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

--------------------------------------
# How to Start this project
1. source umamaheswar/bin/activate
2. python managae.py runserver : to run locally


# Deploy on heroku
1.

# Things to do:
[] Check for image upload
[] only shakha data has been loaded
[] library data need to load
[] Multiple update for single field
[] Select multiple swaymsevak and copy/print there specific field.
[] Remove duplicate.
[] Warn for duplicate during insert new.
[] Add basti wise list and its new page.
[] Basti/Shakha/Ghosh/Gatnayak/Jimmedari wise export in pdf.
[] Add email feature (~/Desktop/trash/gmail.py) and cronjob for birthday greetings.
Issues
1. Shows error on swaymsevak ganvesh count update.
2. Basti number is there not there name. 

# Tips
1. https://github.com/kraiz/django-crontab for crontab in django


# Authentication
Heroku app
oyearunpal@gmail.com
1234@Heroku

# Connecet db through terminal
heroku pg:psql -a umamaheswar
# DB backup
https://devcenter.heroku.com/articles/heroku-postgres-backups