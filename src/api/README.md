
# Deploy instructions

## Standalone debug

    FLASK_APP=api/nearest.py flask run --host=0.0.0.0

Test with:

    http --json POST http://smartjump.ovh:5000/nearest latitude=34.23 longitude=11.22 precision=34

## Nginx production

Read and fight with these files:

- [smartjump-api.ini](https://github.com/smartjump/backend/blob/master/smartjump-api.ini)
- [smartjump-api.uwsgi.service](https://github.com/smartjump/backend/blob/master/smartjump-api.uwsgi.service)
- [wsgi.py](https://github.com/smartjump/backend/blob/master/wsgi.py)

Test with:

    http --json POST http://smartjump.ovh/nearest latitude=34.23 longitude=11.22 precision=34

