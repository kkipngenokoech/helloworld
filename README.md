to install a virtual environment for this project you follow the following steps
you first have to ensure that pipenv is installed - #pip3 install pipenv
step two cd into the directory where you are creating the django project
then you pipenv install django==(version number)2.1
then you pipenv shell- used to start the django environment and make it up and running
now that our environment is up and running we create a django project
django-admin startproject helloworld . =make sure to include the helloworld (.) as this shows that you want it to be installed in the current working directory and should not create anew directory

when we create a django project in our current working directory it creates a couple of files for us
# manage.py
it is used to execute various django commands such as running the server in your local browser
or creating a new app

when you cd into the helloworld folder created it has also some couple of files which include
# settings.py 
contains our project's settings 
# urls.py
tells django which pages to build in response of a url request
# wsgi.py
it stands for web server gateway interface
helps django serve our eventual web pages

it was noting that django is a collection of various applications which when combined makes up the web application
to create an app in django you:
python manage.py startapp pages

# startapp
after this command is executed it creates a couple of python files in the pages sub folder
first up is the :
# admin.py
this is a configuration file for a bulit in django admin application
# apps.py
configuration file of the app itself
# migrations/
it keeps track of any changes of our models.py file so our models.py stay in syc
# models.py 
is where we define our database models, which django automatically translates it to database tables
# test.py
is for our app specific tests
# views.py
is where we handle the request/response logic for our web apps
# NB
we must tell the outer project that this application exists and hence we must add this app to our list of installed applications in the settings.py file in the explicit folder -  order matters hence we have to place the app first so as to have an higher precedence.

# views and URLconfigs
# views: determines what content is displayed on a given page
# URLS: determines where the content is going to 
When a user requests a specific page, like the homepage, the URLConf uses a regular
expression to map that request to the appropriate view function which then returns
the correct data.
# NB ensure also to update your urls for apps in the main url.py