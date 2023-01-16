import sys
from getpass import getpass

from webapp import create_app
from webapp.user.models import User, db

app = create_app()

with app.app_context():
    username = input('Enter username: ')

    if User.query.filter(User.username == username).count():
        print('User already exists')
        sys.exit(0)
    password1 = getpass('Enter password: ')
    password2 = getpass('Reenter password: ')

    if password1 != password2:
        print('Passwords are not the same!')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('User id[{0}] created'.format(new_user.id))