# Django Polls exercise

![Project Logo](docs/static/images/64x64.png "Project Logo")

This project was developed for fun and training during Covid's quarenteen. 
It implements a polling web application.  
The base for this project can be found 
[here](https://docs.djangoproject.com/pt-br/1.11/intro/tutorial01/). 
This solution was improved since the tutorial.

## Development

This project was developed inside a customized slim debian docker container 
with Python 3.6 and virtualenv, using Django and SQLite.

## Dependencies

Python 3.6
Python pip 20.1.1
\+ requirements.txt

## Instructions

**Initialize virtualenv:**

    $ virtualenv .venv
    $ source .venv/bin/activate

**Install project's requirements:**

    $ pip install -r requirements.txt

<!--
**Check if 'task/data/config.py' exists. If doesn't, copy from 'task/data/config.py.tpl':**

    $ cp -i task/data/config.py.tpl task/data/config.py

**Structure a SQLite3 database and transfer data from csv:**  
&#x1F538; *SQLite database will be replaced, if exists.*

    $ python task/sqlite3_prepare_and_transfer_data.py

**Serve the database data in a web application:**  
&#x1F539; *Run the next line and browse http on port 8080 (default).*

    $ python task/web_application.py 8080
-->

**Browse http to Django's admin console to update polls and choices:**  
&#x1F539; [http://localhost:8080/admin](http://localhost:8080/admin)  

**Browse http at the used port to start application:**  
&#x1F539; [http://localhost:8080/](http://localhost:8080/)  

## Information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
"Project Logo" is a free icon from [Icon Shop](https://freeiconshop.com/icon/task-complete-icon-flat/), as described by the site's [license](https://freeiconshop.com/icon-shop-license/).  
"Background" if a free image from [WH Compare](https://whcompare.com). As described in ther site: "This can be freely used on website designs and web design themes available for resale or for free redistribution".

