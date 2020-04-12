from app import blueprint, api
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import json
from app.main import create_app, db
import os
from app.main.model.candidate import Candidate
from app.main.model.candidate_tech import Candidate_Tech

app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def postman():
    """Creates postman.json file"""
    api_data = api.as_postman(urlvars=False, swagger=True)
    postman_file_path = './postman.json'
    if os.path.exists(postman_file_path):
        os.remove(postman_file_path)

    with open(postman_file_path, "w") as fp:
        fp.write(json.dumps(api_data))


@manager.command
def run():
    """ Runs server """
    app.run()


if __name__ == '__main__':
    manager.run()
