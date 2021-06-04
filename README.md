# django_blog_project

# General informations

This is my Blog project.   

In this project User can add new post, change, delete, update and read posts. 

Available registration, that User can register, login, logout.  

User can change Profile Image, and personal information.  

Also available pagination that User can easily find some post.   

User or Clien can send Email that I will receive. 


In this project I used Generic Views and function views, also created signals for saving Profile image, and created Custom User for more comfortable work with Users. 

# Setup

To run this project firstly clone it (in command line):

git clone https://github.com/aaaivanko/django_blog_project.git

Activate virtual environment.

Activation for windows: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html

than install requirements

pip install -r requirements.txt

after that run migrations

python manage.py migrate

and finally

python manage.py runserver

