## Django_api 

This api is designed for an e-commerce aplication.

#### 1. Downloading the application

To download the application you need git installed in you computer.

In the terminal, execute this command to download:

git clone https://github.com/rodolfoguner/django_api

After downloading the application, run:

python -m venv venv

Activate the virtualenv with: 

* In Linux:
source venv/bin/activate

* In Windows:
activate

And then install the requirements of this project, using:

pip install -r requirements.txt

### 2. Testing the application

#### 2.1 Starting the server

To start the server you need to execute:

python manage.py makemigrations

Then:

python manage.py migrate 

And: 

python manage.py runserver

