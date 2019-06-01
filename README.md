[![Build Status](https://travis-ci.com/NickMns/mango.svg?branch=master)](https://travis-ci.com/NickMns/mango)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/Naereen/StrapDown.js.svg)](https://github.com/NickMns/mango/graphs/contributors/)
[![Percentage of issues still open](http://isitmaintained.com/badge/open/nickmns/mango.svg)](http://isitmaintained.com/project/nickmns/mango "Percentage of issues still open")
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/nickmns/mango.svg)](http://isitmaintained.com/project/nickmns/mango "Average time to resolve an issue")

# Mango

A centralized system for HR Outsourcing companies. *Mango* allows outsourcing teams to improve their workflow, and increase their productivity,<br>
by streamlining the bulk of hiring process tasks, thus allowing consultants and managers to focus on matching candidates with companies.<br>
Through the use of our mobile client, applicants can apply to specific job postings and monitor the progress of their request (sheduled interviews,<br>
tests, notifications). 

_*Final deliverable for CN 7021*_

# Table of contents
<details>
<summary>Click here to expand contents</summary>

- [Mango](#mango)
- [Table of contents](#table-of-contents)
- [Get Started](#get-started)
  - [Source Code](#source-code)
  - [Branches](#branches)
  - [Sub-projects](#sub-projects)
- [Sub-Projects](#sub-projects)
  - [Web API](#web-api)
  - [Database](#database)
  - [WPF Client](#wpf-client)
  - [Flutter Client](#flutter-client)
  - [Screenshots](#screenshots)

</details>

# Get Started

## Source Code

Start by cloning the repository from github<br>

```sh
# Get source code from Github
$ git clone https://github.com/NickMns/mango.git
```

## Branches

**master** branch is used for development<br>
**release** branch contains major releases<br>


## Sub-projects

The repository contains a total of three (3) different sub-projects.

| dir               | Sub-project           |   Language        |
|-------------------|-----------------------|---------------    |
|mango-api          |REST API               |Python (Flask)     |
|mango-win-client   |Native Windows Client  |C# (.NET 4.7, WPF) |
|mango_flutter_app  |Mobile Client          |Dart (Flutter)     |

For intstruction on how to build each sub-project consult sections below.

# Sub-Projects

## Web API

The REST API application is written in Python (3.6) using the [Flask](http://flask.pocoo.org/) framework and various other Flask extensions for security,ORM & API implementation.

In order to run the Web API locally you need Python (> 3.6) and pipenv for virtual environment management.

```sh
# Check python version
$ python --version

# Check if pipenv is already installed
$ pip list

# Install pipenv - skip if already installed
$ pip install pipenv

# Change directory
$ cd mango-api

# Setup virtual environment
$ pipenv install
```

The python project makes use of [dotenv](#https://pypi.org/project/python-dotenv/) to dynamically load environment variables from a special file named .env<br>
This file is ignored by git as it contains environment specific variables.

```sh
# create file .env
$ touch .env

# Use nano or any other text editor to edit the file
$ nano .env

# The file must contain the following entries
export ENV="development"
export FLASK_APP="app.py"
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://<username>:<password>@<dbstring>/<dbname>"
export SQLALCHEMY_TRACK_MODIFICATIONS="False"
export FLASK_SECRET_KEY="<dev-secret-key>"
```

_More on Database setup later_

We can now start our local API and add new features or test existing ones.

```sh
# pipenv allows to either start a new shell inside the virtual env or run single commands

$ pipenv shell # Starts a new shell
$ pipenv run <command> # Run single command inside venv

# To run the flask app we can use the built-in command *flask run*
$ pipenv run flask run
Loading .env environment variables…
 * Serving Flask app "app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Our API is now running. We can use curl or more specialized API testing tools (e.g. Postman) to send requests.

## Database

*Mango* uses [PostgreSQL](#https://www.postgresql.org/) as its main relational Database. Depending on whether your dev environment is Windows, Linux or MacOS, the process of setting up the Database locally can be quite different, so it's wise to consult the offical documentation for this step.

After you have completed installation of PostgreSQL in your local environment, you have to create the database that will be used by the system.<br>
(the database will be execute the schema migration process).

One final step before we execute the schema migration is to update our .env file, and more specifically our DATABASE_URL env var, so that it points to our newly created database.<br>

The database migration can now start.

```sh
# Our API project makes use of SQLAlchemy and Alembic for DB entities and management.
# A special script named manage.py is used to execute all db related operations (migrations, upgrade, downgrade, execution, etc)
$ pipenv run python manage.py db upgrade
```

If the migration process finishes without errors it will mean that the new local DB has the latest schema defined in the */migration/version* dir

## WPF Client

In order to build the WPF client you need to have .NET framework 4.7 or newer install along with WPF components for Visual Studio.<br>
The develop/build process is handled primarily through Visual Studio (version 2017 or later) and can only be executed in Windows machines (for now at least).

## Flutter Client

The mobile client for *Mango* is developed using Dart (v2.1.0) and Flutter Framework (v1.0.0). Flutter allows us to use the same codebase for both Android and iOS platforms with only minor tweaks.

To build the project you need the following:

|Name               |   Link                                                                        |
|-------------------|-------------------------------------------------------------------------------|
|JDK                | [Download Page](#https://www.oracle.com/technetwork/java/javase/downloads)    |
|Flutter SDK        | [Download Page](#https://flutter.dev/docs/get-started/install/windows)       |
|Dart SDK           | [Download Page (Optional)](#https://dart.dev/tools/sdk) - Covered by Flutter                  |

As Dart SDK is not mandatory (Flutter contains Dart), we can just need to install JDK and Flutter using the official instruction manuals.<br>
Finally we can install Android Studio (if its not installed).<br>

To check if installation was successfull we can use the following command.

```sh
# Run diagnostic for flutter
$ flutter doctor

# Common issues include misplaced %JAVA_HOME% var and wrong version of JDK installed
```

We are now ready to build the application and deploy it to an emulated device or an actual smartphone.

```sh
# Build the app - either for Android os iOS
$ flutter build <apk> OR <ios>

# List available devices
$ flutter devices

# Install application on attached device
$ flutter install <device>
```

## Screenshots

![Alt text](/screenshots/Client_WPF.png?raw=true "Windows Client")<br>
![Alt text](/screenshots/Client_Mobile.png?raw=true "Mobile Client")