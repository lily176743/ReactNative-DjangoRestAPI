# React-Native and Django Rest API

React Native and Django Rest Framework (Mongodb & SQL)

Rest Framework is located at django-program folder as the backend


Prerequisites
Before you begin, you should have a non-root user with sudo privileges available on your Ubuntu 20.04 server. To set this up, follow our Ubuntu 20.04 initial server setup guide.

Global Install from Packages
If you wish to install Django using the Ubuntu repositories, the process is very straightforward.

First, update your local package index with apt:



Next, check which version of Python you have installed. 20.04 ships with Python 3.8 by default, which you can verify by typing:

python3 -V

You should see output like this:

Output
Python 3.8.2
Next, install Django:

sudo apt install python3-django

You can test that the installation was successful by typing:

django-admin --version

Output
2.2.12
This means that the software was successfully installed. You may also notice that the Django version is not the latest stable version. To learn more about how to use the software, skip ahead to learn how to create sample project.

Install with pip in a Virtual Environment
The most flexible way to install Django on your system is within a virtual environment. We will show you how to install Django in a virtual environment that we will create with the venv module, part of the standard Python 3 library. This tool allows you to create virtual Python environments and install Python packages without affecting the rest of the system. You can therefore select Python packages on a per-project basis, regardless of conflicts with other projects’ requirements.

Let’s begin by refreshing the local package index:

sudo apt update

Check the version of Python you have installed:

python3 -V

Output
Python 3.8.2
Next, let’s install pip and venv from the Ubuntu repositories:

sudo apt install python3-pip python3-venv

Now, whenever you start a new project, you can create a virtual environment for it. Start by creating and moving into a new project directory:

mkdir ~/newproject
cd ~/newproject

Next, create a virtual environment within the project directory using the python command that’s compatible with your version of Python. We will call our virtual environment my_env, but you should name it something descriptive:

python3 -m venv my_env

This will install standalone versions of Python and pip into an isolated directory structure within your project directory. A directory will be created with the name you select, which will hold the file hierarchy where your packages will be installed.

To install packages into the isolated environment, you must activate it by typing:

source my_env/bin/activate

Your prompt should change to reflect that you are now in your virtual environment. It will look something like (my_env)username@hostname:~/newproject$.

In your new environment, you can use pip to install Django. Regardless of your Python version, pip should just be called pip when you are in your virtual environment. Also note that you do not need to use sudo since you are installing locally:


Frontend with React native
-----------------------------


Application layout
We will begin by initialising a authapp/src directory and subdirectories that will contain all our application code and components.

mkdir -p ./src/components
Our application will consist of three screens:

1 - Login screen
2 - Registration screen
3 - Home screen (will serve as the logout screen)
For this we will be using the react-native-router-flux package, based on react navigation.

npm install --save react-native-router-flux
In order to issue the network requests, React Native provides access to the Fetch API out of the box, instead we will be using the axios package as it has some neater features out of the box, such as automatic transformation of JSON data.

npm install --save axios
Ok, we’re ready to start writing some React Native at this point.

# How to install Django¶
This document will get you up and running with Django.

# Install Python¶
Django is a Python web framework. See What Python version can I use with Django? for details.

Get the latest version of Python at https://www.python.org/downloads/ or with your operating system’s package manager.

Python on Windows

If you are just starting with Django and using Windows, you may find How to install Django on Windows useful.

Install Apache and mod_wsgi¶
If you just want to experiment with Django, skip ahead to the next section; Django includes a lightweight web server you can use for testing, so you won’t need to set up Apache until you’re ready to deploy Django in production.

If you want to use Django on a production site, use Apache with mod_wsgi. mod_wsgi operates in one of two modes: embedded mode or daemon mode. In embedded mode, mod_wsgi is similar to mod_perl – it embeds Python within Apache and loads Python code into memory when the server starts. Code stays in memory throughout the life of an Apache process, which leads to significant performance gains over other server arrangements. In daemon mode, mod_wsgi spawns an independent daemon process that handles requests. The daemon process can run as a different user than the web server, possibly leading to improved security. The daemon process can be restarted without restarting the entire Apache web server, possibly making refreshing your codebase more seamless. Consult the mod_wsgi documentation to determine which mode is right for your setup. Make sure you have Apache installed with the mod_wsgi module activated. Django will work with any version of Apache that supports mod_wsgi.

See How to use Django with mod_wsgi for information on how to configure mod_wsgi once you have it installed.

If you can’t use mod_wsgi for some reason, fear not: Django supports many other deployment options. One is uWSGI; it works very well with nginx. Additionally, Django follows the WSGI spec (PEP 3333), which allows it to run on a variety of server platforms.

Get your database running¶
If you plan to use Django’s database API functionality, you’ll need to make sure a database server is running. Django supports many different database servers and is officially supported with PostgreSQL, MariaDB, MySQL, Oracle and SQLite.

If you are developing a small project or something you don’t plan to deploy in a production environment, SQLite is generally the best option as it doesn’t require running a separate server. However, SQLite has many differences from other databases, so if you are working on something substantial, it’s recommended to develop with the same database that you plan on using in production.

In addition to the officially supported databases, there are backends provided by 3rd parties that allow you to use other databases with Django.

In addition to a database backend, you’ll need to make sure your Python database bindings are installed.

If you’re using PostgreSQL, you’ll need the psycopg2 package. Refer to the PostgreSQL notes for further details.
If you’re using MySQL or MariaDB, you’ll need a DB API driver like mysqlclient. See notes for the MySQL backend for details.
If you’re using SQLite you might want to read the SQLite backend notes.
If you’re using Oracle, you’ll need a copy of cx_Oracle, but please read the notes for the Oracle backend for details regarding supported versions of both Oracle and cx_Oracle.
If you’re using an unofficial 3rd party backend, please consult the documentation provided for any additional requirements.
If you plan to use Django’s manage.py migrate command to automatically create database tables for your models (after first installing Django and creating a project), you’ll need to ensure that Django has permission to create and alter tables in the database you’re using; if you plan to manually create the tables, you can grant Django SELECT, INSERT, UPDATE and DELETE permissions. After creating a database user with these permissions, you’ll specify the details in your project’s settings file, see DATABASES for details.

If you’re using Django’s testing framework to test database queries, Django will need permission to create a test database.

# Install the Django code¶
Installation instructions are slightly different depending on whether you’re installing a distribution-specific package, downloading the latest official release, or fetching the latest development version.

Installing an official release with pip¶
This is the recommended way to install Django.

Install pip. The easiest is to use the standalone pip installer. If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.

Take a look at venv. This tool provides isolated Python environments, which are more practical than installing packages systemwide. It also allows installing packages without administrator privileges. The contributing tutorial walks through how to create a virtual environment.

After you’ve created and activated a virtual environment, enter the command:

/ 
$ python -m pip install Django
Installing a distribution-specific package¶
Check the distribution specific notes to see if your platform/distribution provides official Django packages/installers. Distribution-provided packages will typically allow for automatic installation of dependencies and supported upgrade paths; however, these packages will rarely contain the latest release of Django.

# Installing the development version¶
Tracking Django development

If you decide to use the latest development version of Django, you’ll want to pay close attention to the development timeline, and you’ll want to keep an eye on the release notes for the upcoming release. This will help you stay on top of any new features you might want to use, as well as any changes you’ll need to make to your code when updating your copy of Django. (For stable releases, any necessary changes are documented in the release notes.)

If you’d like to be able to update your Django code occasionally with the latest bug fixes and improvements, follow these instructions:

Make sure that you have Git installed and that you can run its commands from a shell. (Enter git help at a shell prompt to test this.)

Check out Django’s main development branch like so:

/ 
# $ git clone https://github.com/django/django.git
This will create a directory django in your current directory.

Make sure that the Python interpreter can load Django’s code. The most convenient way to do this is to use a virtual environment and pip. The contributing tutorial walks through how to create a virtual environment.

After setting up and activating the virtual environment, run the following command:

/ 
# $ python -m pip install -e django/
This will make Django’s code importable, and will also make the django-admin utility command available. In other words, you’re all set!

When you want to update your copy of the Django source code, run the command git pull from within the django directory. When you do this, Git will download any changes.

# Models and databases¶
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

Models
Making queries
Aggregation
Search
Managers
Performing raw SQL queries
Database transactions
Multiple databases
Tablespaces
Database access optimization
Database instrumentation
Examples of model relationship API usage
