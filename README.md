# Django Polls

![Project Logo](docs/static/images/64x64.png "Project Logo")

This project was developed for fun and training and implements a simple polling web application.  
'[Writing your first Django app](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)' 
is where this exercise starts at. Still playing, so I don't know where it ends.

## Development

This project was developed inside a customized slim debian docker container 
with Python 3.6 and virtualenv, using Django and SQLite.

## Dependencies

Python 3.6  
Python pip 20.1.1  
\+ requirements.txt

## Instructions  

**Clone and enter this project:**  

    $ git clone https://github.com/nandoabreu/django-poll.git
    $ cd django-poll

**Initialize virtualenv:**

    $ virtualenv .venv
    $ source .venv/bin/activate

**Install requirements:**

    $ pip install -r requirements.txt

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
> Check prerequisites and commands from [Deploying a Django application](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-deploy).  
> Because of the sqlite version in Python 3.6 in Amazon Linux, we will deploy in Amazon Linux **2** with Python 3.7.

    $ eb init -p python-3.7 django-poll --region us-east-2
    $ eb init
    $ eb create django-poll-env
    $ echo http://$(eb status | grep CNAME | sed 's/.*: //')
    $ eb open

<!--
**Check if 'task/data/config.py' exists. If doesn't, copy from 'task/data/config.py.tpl':**

    $ cp -i task/data/config.py.tpl task/data/config.py

**Structure a SQLite3 database and transfer data from csv:**  
&#x1F538; *SQLite database will be replaced, if exists.*

    $ python task/sqlite3_prepare_and_transfer_data.py
-->

## Information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
"Project Logo" is a free icon from [Icon Shop](https://freeiconshop.com/icon/task-complete-icon-flat/), as described by the site's [license](https://freeiconshop.com/icon-shop-license/).  
"Background" if a free image from [WH Compare](https://whcompare.com). As described in ther site: "This can be freely used on website designs and web design themes available for resale or for free redistribution".

