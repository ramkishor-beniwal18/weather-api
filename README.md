## Environment:
- Python version: 3.7
- Django version: 3.0.6
- Django REST framework version: 3.11.0

## Read-Only Files:
- rest_api/tests.py
- manage.py

## Data:
Example of a weather data JSON object:
```
{
   "id": 1,
   "date": "1985-01-01",
   "lat": 36.1189,
   "lon": -86.6892,
   "city": "Nashville",
   "state": "Tennessee",
   "temperature": 17.3
}
```

## Requirements:
The REST service must expose the /weather/ endpoint, which allows for managing the collection of weather records in the following way:


POST request to `/weather/`:
- creates a new weather data record
- expects a valid weather data object as its body payload, except that it does not have an id property; you can assume that the given object is always valid
- adds the given object to the collection and assigns a unique integer id to it
- the response code is 201 and the response body is the created record, including its unique id

GET request to `/weather/`:
- the response code is 200
- the response body is an array of matching records, ordered by their ids in increasing order

GET request to `/weather/<id>/`:
- returns a record with the given id
- if the matching record exists, the response code is 200 and the response body is the matching object
- if there is no record in the collection with the given id, the response code is 404

DELETE request to `/weather/<id>/`:
- deletes the record with the given id from the collection
- if matching record existed, the response code is 204
- if there was no record in the collection with the given id, the response code is 404

Your task is to complete the given project so that it passes all the test cases when running the provided unit tests. The implementation of the model is already provided. The project by default supports the use of the SQLite3 database. Implement the `POST` request to `/weather/` first because testing the other methods require `POST` to work correctly.

## Commands

+ run:
```source env1/bin/activate; pip3 install -r requirements.txt; python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb && python3 manage.py runserver 0.0.0.0:8000```

+  install:
```bash python_install.sh;source env1/bin/activate; pip3 install -r requirements.txt;```

+ test:
```rm -rf unit.xml;source env1/bin/activate; python3 manage.py test```
