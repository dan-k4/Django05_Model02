
import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
setup()

from ModelApp.models import Person

# all
persons = Person.objects.all()
for person in persons:
    print(person.id, person, person.salary)

# person = Person.objects.get(first_name = 'taro')
person = Person.objects.get(pk=1)
print(person.id, person)

# filter
print('*'*50)
persons = Person.objects.filter(first_name='taro').all()
print(persons)

print(persons[0].email)
for person in persons:
    print(person.id, person)
