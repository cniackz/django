# Steps to get things working
1. `cd /Users/ccelis/django/mysite`
1. `source ~/django/.venv/bin/activate`
1. `python manage.py runserver`
1. `http://127.0.0.1:8000/`
1. `http://127.0.0.1:8000/quickstart/` 
   * Full Stack Testing
   * PSQL <-> BE <-> API <-> FE
1. `http://127.0.0.1:8000/questions/`
   * API Testing
   * PSQL <-> BE <-> REST Framework
1. `http://127.0.0.1:8000/polls/`
   * No API implementation
   * PSQL <-> BE <-> FE

# PSQL

To connect to my database:
`psql -h localhost -p 5432 -U ccelis cesar`

# Python Virtual Environment

To activate my virtual environment:
`source ~/django/.venv/bin/activate`

| Package             | Version |
| ------------------- |:-------:|
| asgiref             | 3.3.1   |
| Django              | 3.1.3   |
| pip                 | 20.2.4  |
| psycopg2-binary     | 2.8.6   |
| pytz                | 2020.4  |
| setuptools          | 41.2.0  |
| sqlparse            | 0.4.1   |
| djangorestframework | 3.12.2  |

# Django Admin

* Username: admin
* Password: Yuyu@123

# API 
## GET Questions
### Documentation: 
https://www.django-rest-framework.org/tutorial/quickstart/
#### curl
`curl -H 'Accept: application/json; indent=4' -u admin:Yuyu@123 http://127.0.0.1:8000/questions/`
#### JavaScript
https://stackoverflow.com/questions/247483/http-get-request-in-javascript
```
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
```
# Django User Interface
* You can select one question:
  * `http://127.0.0.1:8000/polls/`
* You can vote for each question:
  * `http://127.0.0.1:8000/polls/2/`
* You can see the results for each voted question
  * `http://127.0.0.1:8000/polls/2/results/`

# Authentication credentials were not provided.
If you see this message on http://127.0.0.1:8000/questions/ \
You need to login, if you open up the browser you'll see a 'Login' \
link in the top right of the page. If you log in as admin/Yuyu@123, \
you'll be able to to see the data.
