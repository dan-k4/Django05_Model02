import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

p = Person(
    first_name='taro', last_name='yamada',
    birthday= '2000-01-01', email='taro@email.com',
    salary=100000, memo='taro test', web_site='http://taro.com'
)
p = Person(
    first_name='taro', last_name='yamada',
    birthday='2000-01-01', email='taro@email.com',
    salary=None, memo='taro test', web_site='http://taro.com'
)

p = Person(
    first_name='taro', last_name='yamada',
    birthday='2000-01-01', email='taro@email.com',
    salary=None, memo='taro test', web_site=''
)

# p.save()

# class method create

# Person.objects.create(
#     first_name='shinzo', last_name='abe',
#     birthday='1987-09-08', email='shinzo@email.com',
#     salary=300000000, memo='shinzo test', web_site='http://NHK.co.jp',
# )

# get_or_create

obj, created = Person.objects.get_or_create(
    first_name='shinzo', last_name='abe',
    email='shinzo@email.com',
    salary=5000, memo='shinzo test', web_site='http://NHK.co.jp',
)

print(obj)
print(created)
