import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()

import random
from app_2.models import AccessRecord, WebPage, Topic
from faker import Faker


fakegen = Faker()

topics = [
    'Search', 'Social', 'Nature', 'Marketplace',
    'Knitting', 'News', 'Tech', 'Games'
]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get topic for the entry
        top = add_topic()
        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        # create new webpage entry
        webpg = WebPage.objects.get_or_create(
            topic=top,
            url=fake_url,
            name=fake_name
        )[0]
        # create fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg,
            date=fake_date
        )[0]


if __name__ == '__main__':
    print('pop script!')
    populate(20)
    print('pop complete!')
    
