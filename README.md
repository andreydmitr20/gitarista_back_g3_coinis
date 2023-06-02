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
<h3> Tools </h3>
<br>
    Postman
    Dbeaver

<h3> API </h3>
<br>
<p>
    Schemas:

    http://127.0.0.1:8000/api/schema/
    http://127.0.0.1:8000/api/schema/swagger-ui/
    http://127.0.0.1:8000/api/schema/redoc/

    API:

    http://127.0.0.1:8000/api-auth/
    http://127.0.0.1:8000/song/

    Note that it is for back-enders only:
    http://127.0.0.1:8000/admin/

</p>
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
