# Django Polls into AWS EB (Amazon Elastic Beanstalk)

![Project Logo](docs/static/images/64x64.png "Project Logo")

This project was developed for fun and training and delivers 
a simple polling web application made with Python Django 
([Writing your first Django app](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)). 
This repository holds the project implementation running locally and 
**intends to guide the deploy into AWS EB**.

## Development

This project was developed inside a customized slim debian docker container 
with Python 3.6 and virtualenv, using Django and SQLite. It was all coded and commanded via Vim, 
Git shell (see [Atlassian's 'Install Git'](https://www.atlassian.com/git/tutorials/install-git) 
for instructions) and EB Cli command line 
(see [Amazon's 'Install the EB CLI'](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) 
for instructions).

## Dependencies for local execution

Python 3.6 (works on 3.7)  
Python pip 20.1.1  
\+ requirements.txt

## Tools for Git download and EB deploy

Git 2.20.1  
EB CLI 3.18.1  

## Instructions  

**Clone and enter this project:**  

    $ git clone https://github.com/nandoabreu/django-polls.git
    $ cd django-polls

**Initialize virtualenv:**

    $ virtualenv .venv
    $ source .venv/bin/activate

**Install and configurate:**

    $ pip install -r requirements.txt
    $ python manage.py collectstatic --noinput

**Start the server:**  

    $ python manage.py runserver 0:8080

**Login admin console to update Questions:**  
```
http://localhost:8080/admin  
Username: admin  
Password: poll2020
```

**Browse the poll:**  
```
http://localhost:8080/  
```

**Deploy the application in AWS Elastic Beanstalk**  
> Prerequisites and commands can be found at [Deploying a Django application](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-deploy) .  
> Because of the sqlite module version in Amazon Linux, we will deploy 
this solution in Amazon Linux **2** with Python 3.7.

    $ eb init -p python-3.7 django-polls --region us-east-2
    $ eb init
    $ eb create django-polls-env
    $ echo http://$(eb status | grep CNAME | sed 's/.*: //')
    $ eb open

## Information

An issue about this deploy is that once it is published via AWS EB, static files 
(like style.css) are not read and the page lacks on style. Documents and forums 
are not very clear on pointing out this is a Django way of deploying 
and the web server must be instructed to use these files are served.

Once `STATIC_ROOT` and `STATIC_URL` are defined inside `project/settings.py` and 
added to `urlpatterns` inside `project/urls.py`, the problem is solved.

> ***STATIC_ROOT*** holds the path where from the static files will be served.  
> ***collectstatic*** will place app and admin files inside STATIC_ROOT.  
> ***STATIC_URL*** holds the link to STATIC_ROOT, when requested from the browser.  
> ***\+ static(settings[...]*** tells the web server that STATIC_URL is to be used.

## Licenses

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
- Django is licensed under the Django's BSD license - 
visit [djangoproject.com](https://www.djangoproject.com/foundation/faq/) to know more.  
- "Project Logo" is a free icon from 
[Icon Shop](https://freeiconshop.com/icon/task-complete-icon-flat/), 
as described by the site's [license](https://freeiconshop.com/icon-shop-license/).  
- "Background" if a free image from 
[WH Compare](https://whcompare.com). As described in ther site: 
"This can be freely used on website designs and web design themes 
available for resale or for free redistribution".

