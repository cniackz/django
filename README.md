# Steps to get things working
`cd /Users/ccelis/django/mysite`
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
