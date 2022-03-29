from faker import Faker
from random import randint

# Todo, Tests and mutations

def generate_random_user_data(faker_object, filename="example-user-data.csv", num_of_records=1000):
    """Write a new file with first_name, last_name, email, and company.

    Keyword arguments:
    faker_object
    filename -- name of file you are writing to or overwriting
    """
    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{},{}\n".format(fake.first_name(), fake.last_name(), fake.email(), fake.company()))

def generate_random_ip_data(faker_object, filename="example-ip-data.csv", num_of_records=1000):
    """Writes a new file with ipv4 address, user_agent, and past datetime.

    Keyword arguments:
    faker_object
    filename -- name of file you are writing to or overwriting
    """
    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{}\n".format(fake.ipv4(), fake.user_agent(), fake.past_datetime()))

def generate_sensitive_user_data(faker_object, filename="example-sensitive-user-data.csv", num_of_records=1000):
    """Writes a new file with a user_name, password, and email.

    Keyword arguments:
    faker_object
    filename -- name of file you are writing to or overwriting
    """
    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{}\n".format(fake.user_name, fake.password(), fake.email()))

def generate_random_bank_account_data(faker_object, filename="example-bank-account-data.csv", num_of_records=1000):
    """Writes a new file with a name, company, city, and random integer.

    Keyword arguments:
    faker_object
    filename -- name of file you are writing to or overwriting
    """
    with open(filename, 'w') as the_file:
        for i in range(num_of_records):
            the_file.write("{},{},{},{}\n".format(fake.name(), fake.company(), fake.city(), randint(10000000, 999999999)))

if __name__ == "__main__":

    fake = Faker()

    generate_random_user_data(fake, "dummy-user-data2.csv", 25000)

    generate_random_ip_data(fake, "dummy-ip-data.csv", 25000)

    generate_sensitive_user_data(fake, "dummy-sensitive-user-data.csv", 25000)

    generate_random_bank_account_data(fake, "dummy-bank-account-data.csv", 25000)
