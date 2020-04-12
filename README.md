## Basic API for Candidates and Admins

Python implementation of some basic API for candidates and administrators.

#### Running project
- Configuration is located at `app/main/config.py`
    - Currently using `sqlite` as database, because of easy setup and portability.
- By default when app is run on `localhost:5000` is available full swagger documentation.

##### Database initialization
For database interaction and migrations are used `SQLAlchemy` and `Alembic`.
- To apply migrations run: `python manage.py db upgrade`

##### Running project 
Server is run with `python manage.py run`

##### Generate postman.json
To generate `postman.json` collection dump user `python manage.py postman`

##### Manage
Everything regarding project is run through `manage.py`. For more info type `python manage.py --help` each subcommand has its own help as well.
      
