from django.test import TestCase

# Create your tests here.
from faker  import Faker # faker is the class
fake= Faker()  # fake is object
name=fake.name()
first_name=fake.first_name()
last_name=fake.last_name()
email=fake.email()
city=fake.city()
addr=fake.address()

print(name,first_name,last_name,email,city,addr,sep='\n')