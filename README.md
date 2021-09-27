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
venv/Scripts/activate

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


#### 2.2 Executing test with postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/17577871-bd624e35-4eaf-4a06-b5e8-04407e464349?action=collection%2Ffork&collection-url=entityId%3D17577871-bd624e35-4eaf-4a06-b5e8-04407e464349%26entityType%3Dcollection%26workspaceId%3D8d12c232-b3d7-41a9-9248-b940c09757fd)


Testing update and delete is necessary to change the ID in the link of the registration:

Example:

http://127.0.0.1:8000/client/2/ 

and change 

http://127.0.0.1:8000/client/3/

If the ID don't exist.
