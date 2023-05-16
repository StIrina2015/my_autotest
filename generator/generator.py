from faker import Faker
import random
from data.data import Person

faker_en = Faker('en_US')
Faker.seed()

def get_person():
    yield Person(
        full_name=faker_en.first_name() + ' ' + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address()
 )



