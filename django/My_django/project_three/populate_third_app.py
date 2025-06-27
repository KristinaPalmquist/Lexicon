import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_three.settings')
django.setup()

import random
from third_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fake_firstname + '.' + fake_lastname + '@' + fakegen.domain_name()
        usr = User.objects.get_or_create(
            firstname=fake_firstname,
            lastname=fake_lastname,
            email=fake_email
        )[0]


if __name__ == '__main__':
    print('pop script!')
    populate(20)
    print('pop complete!')
    
