from app.main.models import User
from app import create_app, db
import os
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager




app = create_app(os.getenv('OPTIMUS_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# # migrations
# manager.add_command('db', MigrateCommand)


# @manager.command
# def create_db():
#     """Creates the db tables."""
#     db.create_all()


# @manager.command
# def drop_db():
#     """Drops the db tables."""
#     db.drop_all()


# @manager.command
# def create_admin():
#     """Creates the admin user."""
#     db.session.add(User(email="evansonmwangi83@gmail.com", password="admin", admin=True))
#     db.session.commit()


# @manager.command
# def create_data():
#     """Creates sample data."""
#     pass


if __name__ == '__main__':
    manager.run()
