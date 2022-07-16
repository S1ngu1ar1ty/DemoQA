from faker import Faker


fake = Faker()

class Student:
    
    def __init__(self, first_name, last_name, email, number, address, date):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.number = number
        self.address = address
        self.date = date.strftime('%d %b %Y')


student = Student(fake.first_name(), fake.last_name(), fake.email(), 
                fake.msisdn()[3:], fake.address(), fake.date_of_birth(minimum_age=18))
