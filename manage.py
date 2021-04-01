# manage.py

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from wsgi import create_app
from app import db

application = create_app()

migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

# create postgres database: twitter_api_flask
# winpty psql -U postgres -c "CREATE DATABASE twitter_api_flask"
# create the file structure that will be used by sqlAlchemie
# pipenv run python manage.py db init
# create script to create my tables :
# pipenv run python manage.py db migrate -m "Create tweets table"
# create my tables :
# pipenv run python manage.py db upgrade
# add some datas :
# pipenv run flask shell
# >>> from app import db
# >>> from app.models import Tweet
# >>> tweet = Tweet(text="Our first tweet!")
# >>> db.session.add(tweet)
# >>> db.session.commit()
# # Did it work?
# >>> db.session.query(Tweet).count()
# >>> db.session.query(Tweet).all()
# # Hooray!