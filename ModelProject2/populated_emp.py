import os,django # os is the  module to register this script with the main project
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject2.settings") 
django.setup()
from Modelapp.models import EmployeeModel
from faker  import Faker # faker is the class
fake= Faker()  # fake is object
def data_gen():
    eid=fake.random_int(100,500)
    ename=fake.name()
    company=fake.company()
    job=fake.job()
    esal=fake.random_int(10000,60000)
    email=fake.email()
    city=fake.city()
    addr=fake.address()
    # to create objects in the database
    EmployeeModel.objects.create(eid=eid,ename=ename,company=company,job=job,esal=esal,email=email,city=city,addr=addr)
    
n=int(input("Enter the Number of records:"))
for i in range(n):
    data_gen()
print(n,"No. of data records are created successfully")

