from faker import Faker
from random import randint

def user_data(filename="example-user-data.csv", num_of_records=1000):
    """Write a new file with first_name, last_name, email, and company.

    Keyword arguments:
    filename -- name of file you are writing to or overwriting (default "example-user-data.csv)
    num_of_records -- Number of dummy records you would like the function to create (default 1000)
    """

    fake = Faker()

    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{},{}\n".format(fake.first_name(), fake.last_name(), fake.email(), fake.company()))

def sensitive_user_data(filename="example-sensitive-user-data.csv", num_of_records=1000):
    """Writes a new file with a user_name, password, and email.

    Keyword arguments:
    filename -- name of file you are writing to or overwriting (default "example-sensitive-user-data.csv)
    num_of_records -- Number of dummy records you would like the function to create (default 1000)
    """

    fake = Faker()

    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{}\n".format(fake.user_name, fake.password(), fake.email()))

def ip_data(filename="example-ip-data.csv", num_of_records=1000):
    """Writes a new file with ipv4 address, user_agent, and past datetime.

    Keyword arguments:
    filename -- name of file you are writing to or overwriting (default "example-ip-data.csv)
    num_of_records -- Number of dummy records you would like the function to create (default 1000)
    """

    fake = Faker()

    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{}\n".format(fake.ipv4(), fake.user_agent(), fake.past_datetime()))


def transaction_data(filename="example-bank-account-data.csv", num_of_records=1000):
    """Writes a new file with a name, company, city, and random integer.

    Keyword arguments:
    filename -- name of file you are writing to or overwriting (default "example-transaction-data.csv)
    num_of_records -- Number of dummy records you would like the function to create (default 1000)
    """

    fake = Faker()

    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{},{}\n".format(fake.name(), fake.company(), fake.city(), randint(10000000, 999999999)))