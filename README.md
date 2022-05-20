# weBlog - Docker & Docker-compose deployment

## WeBlog Studet Blog
The Main branch setups the app to single-host EC2 or Linux server, deployng the Flask application and psql database server on the host.

The docker image has been uploaded to  [`Staffer App`](https://staffer-udacity.herokuapp.com/)

We are implementing a Jinja templated front end (not part of this project) located at  [`Jinja Frontend`](http://udacity-staffer.herokuapp.com/)

The [`Staffer App`](https://staffer-udacity.herokuapp.com/)

1. 
&nbsp;

----

## Setting up the Project from the github repo

### Before you start:
Ensure docker & docker-compose is intalled in the server [Docker on Ubuntu installation](https://docs.docker.com/engine/install/ubuntu/) 


&nbsp;

1. Clone the [repo ](https://www.postgresql.org/download/) into the weblog direcotory

```console
git clone git@github.com:myportfolio-tech/wcBlog.git weblog
```
2. Navigate the project folder 
```console
cd weblog
```
3. Build the image with docker-compose

```console
docker-compose build
```
4. Bring up the docker image
```console
docker-compose up
```

&nbsp;


### Database Setup
With Postgres running, create the database, create tables, and insert innitial data.
```bash
psql postgres < starting_psql_tester.psql
```
&nbsp;


### Running the flask server

The app will run locally on port 5000.


```bash
python wsgi.py
```

Check the app is running [`locally`](http://localhost:5000).

&nbsp;

### Project Structure

```sh
fs-capstone
    ├───migrations
    │   └───versions
    └───staffer
    │   ├───employees
    │   ├─────── _init__.py        
    │   ├───errors
    │   ├─────── _init__.py      
    │   ├───main
    │   ├─────── _init__.py      
    │   ├───projects
    │   ├─────── _init__.py      
    │   ├───utils
    │   ├─────── _init__.py      
    │   │
    │   ├ __init__.py
    │   ├ config.py
    │   ├ models.py
    │
    ├ .env
    ├ manage.py
    ├ test_staffer.py
    ├ wsgi.py

```

&nbsp;

The main module **staffer** contains the modules:

1. employees
2. errors
3. main
4. projects
5. utils

These modules are registered as Blueprints in the staffer module __init__ file


&nbsp;

### Migrations


Because flask_migrate is no longer mantained, this project uses *flask.cli*

If you are migrating to Heroku, you must perform the taasks in the specific order:

Run Locally:
```concole
flask db init
flask db migrate 
```
Commit your changes to github.

Run locally and in Heroku:
```console
flask db upgrade
```

