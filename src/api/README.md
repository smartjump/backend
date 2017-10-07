
# Deploy instructions

## Standalone debug

    FLASK\_APP=api/nearest.py flask run --host=0.0.0.0

Test with:

    http --json POST http://smartjump.ovh:5000/nearest latitude=34.23 longitude=11.22 precision=34

## Nginx production




