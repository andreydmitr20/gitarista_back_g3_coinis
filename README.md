<h1> Back-end for app gitaristi. </h1>
<h2> Group 3 students of Coinis Developers Lab. </h2>
<br>

<h3> Installation </h3>
<br>
<h4> Linux </h4>
<br>
    Install python 3.10.6, then:

    > gh repo clone andreydmitr20/gitarista_back_g3_coinis

    > cd gitarista_back_g3_coinis

    > python3 -m venv venv

    > source venv/bin/activate

    > cd django

    > pip3 install -r requirements.txt

    > python3 m migrate

    > python3 m loaddata ./data/data<last_version>.json

    > python3 m runserver

<h4> Windows </h4>
<br>
<p>
    Install python 3.10.6 https://www.python.org/downloads/release/python-3106/

    Install gh https://github.com/cli/cli/releases/tag/v2.30.0

    Install git https://github.com/git-for-windows/git/releases/tag/v2.40.1.windows.1

    Then in command prompt:

    > gh auth login

    > gh repo clone andreydmitr20/gitarista_back_g3_coinis

    > cd gitarista_back_g3_coinis

    > python.exe -m venv venv

    > venv\Scripts\activate.bat

    > cd django

    > pip.exe install -r requirements.txt

    > python.exe m migrate

    > python.exe m loaddata ./data/data<last_version>.json

    > python.exe m runserver

</p>
<h3> Tests </h3>
<br>
    > pytest

<h3> CORS </h3>
<br>
    We have add <a href="https://github.com/adamchainz/django-cors-headers">django-cors-headers</a>

    So you just need to add your server path inside
    django/gitarista/settings.py like this:

    CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "null",
    ]

<h3> API </h3>
<br>

<p>
    Schemas:

    http://127.0.0.1:8000/api/docs/
    http://127.0.0.1:8000/api/schema/

</p>

    Retrieve (GET) parameters: search, page, page_size, short and more....

    Id=0 means 'All'

    Examples for API version 2 (v2) :

    Get first page of authors:
        GET
        http://127.0.0.1:8000/api/v2/songs/authors/0/

    Get the author with id=23:
        GET
        http://127.0.0.1:8000/api/v2/songs/authors/23/

    Get first page of authors with just some (reduced) data fields count:
        GET
        http://127.0.0.1:8000/api/v2/songs/authors/0/?short=1

    Get authors count with 'Mr' in name:
        GET
        http://127.0.0.1:8000/api/v2/songs/authors/0/?search=Mr&page=0

    Get authors page 10:
        GET
        http://127.0.0.1:8000/api/v2/songs/authors/0/?page=10&page_size=5


    Create an author 'new author':
        POST body={'name'='new author'}
        http://127.0.0.1:8000/api/v2/songs/authors/0/


    Update the name of the author with id=1 to 'new name:
        PUT body={'name'='new name'}
        http://127.0.0.1:8000/api/v2/songs/authors/1/


    Delete author with id=1:
        DELETE
        http://127.0.0.1:8000/api/v2/songs/authors/1/

User Options:

    User register:
        POST body={
            "username": "user",
            "email": "user@user.com",
            "password": "user1234!",
            "password2": "user1234!"
        }
        http://127.0.0.1:8000/api/register/

    User login:
        POST body={
        "email": "user@user.com",
        "password2": "user1234!"
        }
        http://127.0.0.1:8000/api/login/

    User logout:
        POST body={}
        http://127.0.0.1:8000/api/logout/

    User info(logged user):
        GET
        http://127.0.0.1:8000/api/user/

<h3> Relational schema from <a href="erdplus.com">erdplus.com</a> </h3>
<br>
<a href="./docs/gitaristi.erdplus">
    <img src="./docs/relational_schema.png" alt="relational schema">
</a>

<h3> Two back-end parts </h3>
    <ul>
        <li> user part (all about authentication etc.)</li>
        <br>
        <li> song part (all about songs etc.)</li>
    </ul>

<h3> Back-end team members </h3>
    <ul>
        <li> Andrei Osetrov </li>
        <br>
        <li> Nemanja Lakicevic </li>
    </ul>
