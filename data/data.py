from faker import Faker


fake = Faker()

class Student:
    
    def __init__(self, first_name, last_name, email, number, address):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.number = number
        self.address = address


student = Student(fake.first_name(), fake.last_name(), fake.email(), fake.msisdn()[3:], fake.address())
