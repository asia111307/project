# Project


## Built with
- HTML, CSS, JavaScript and [Bootstrap4](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - as a frontend layer
- [Python3.6](https://www.python.org/) - as a backend language
- [Flask](https://palletsprojects.com/p/flask/) - the Python framework
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - the Python SQL toolkit



## Run with virtualenv
You have to install **Python 3.6** on your machine, if you do not have it yet, e.g with: 
    
    $ sudo apt-get install python3.6

Then, install **virtualenv**:

    $ pip install virtualenv 

Create and start **virtual environment**:

    $ source venv/bin/activate && pip install -r requirements.txt

Run **project**:

    $ FLASK_APP=start.py FLASK_DEBUG=1 flask run




